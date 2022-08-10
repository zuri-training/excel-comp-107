from django.shortcuts import render

from excel.models import Document, Post, user_directory_path
from excel.forms import DocumentForm

from django.views.generic.edit import FormView
from django.views import generic

from django.shortcuts import get_object_or_404, render

import pandas as pd
import numpy as np
import os


def home(request):
    return render(request, 'excel/home.html')

def dashboard(request):
    documents = Document.objects.all()
    return render(request, 'excel/dashboard.html', {'documents': documents})

class FileFieldFormView(FormView):
    form_class = DocumentForm
    template_name = 'excel/model_form_upload.html'  # Replace with your template.
    success_url = '/posts'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        post = Post.objects.create(user=request.user)

        if form.is_valid():
            for f in files:
                Document.objects.create(file=f, post=post)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class Posts(generic.ListView):
    template_name = 'excel/posts.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.all()


# returns all(2) documents for a post instance 
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'excel/post_detail.html', {'post': post})

def style_specific_cell(x, item):

    color = 'background-color: lightgreen'
    df = pd.DataFrame('', index=x.index, columns=x.columns)
    df.iloc[item[0], item[1]] = color
    return df

def compare(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        # post = Post.objects.get(id=request.id)
        document_1 = str(post.documents.first().file)
        document_2 = str(post.documents.last().file)

        df1 = pd.read_excel(document_1)
        df2 = pd.read_excel(document_2)

        writer = pd.ExcelWriter(user_directory_path(Document.objects.last(), 'Excel_differ.xlsx'), engine='xlsxwriter')
        df1.to_excel(writer, index=False, header=True, sheet_name='report')

        workbook = writer.book
        worksheet = writer.sheets['report']

        comparison_values = df1.values == df2.values
        rows,cols=np.where(comparison_values==True)
        print (rows, cols)

        for item in zip(rows,cols):
            print("item: ", item)
            df1.iloc[item[0], item[1]] = int('{}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]]))
            s = df1.iloc[item[0], item[1]]
            print(s)

            item = [item for item in zip(rows, cols)]
            print(item)
            print(item[0])
            print(item[1])

            cell_format = workbook.add_format({'bold': True, 'font_color': 'black', 'bg_color': 'yellow'})

            # https://xlsxwriter.readthedocs.io/working_with_conditional_formats.html
            worksheet.conditional_format('A1:XFD1048576', {'type':     'cell',
                                                    'criteria': '=',
                                                    'value':    s, # edit this, it returns all values for all criteria
                                                    'format':   cell_format})

        writer.save()

    return render(request, 'excel/post_detail.html', {'post': post})
