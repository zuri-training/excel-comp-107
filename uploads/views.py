from django.shortcuts import render,redirect
from .forms import ExcelFileForm
import random

# Create your views here.



def model_upload(request):
    if request.method == 'POST':
        form = ExcelFileForm(request.POST, request.FILES)
        key = random.randint(0,99999)

        if form.is_valid():
            return handle_uploaded_file(request, form, request.FILES['file1'], request.FILES['file2'])
        else:
            return alert(request)
    else:
        form = ExcelFileForm()
        return render(request, 'upload/model_upload.html', {'form': form, 'isAlert': False})


def alert(request):
    form = ExcelFileForm()
    return render(request, 'upload/model_upload.html', {'form': form, 'isAlert': True})


def handle_uploaded_file(request, form, f1, f2):
    SUPPORTED_FORMATS = ['xls', 'xlsx', 'csv', 'tsv']
    file1format = f1.name.split('.')[-1]
    file2format = f2.name.split('.')[-1]
    if file1format not in SUPPORTED_FORMATS or file2format not in SUPPORTED_FORMATS:
        return alert(request)
    else:
        form.save()
        return redirect('compare:display_table')

