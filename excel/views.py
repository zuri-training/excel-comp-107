from django.shortcuts import render
from .forms import DocumentForm
from .models import Document


def home(request):
    # documents = Document.objects.all()
    return render(request, 'excel/home.html')

def create_to_feed(request):
    user = request.user
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        file_form = DocumentForm(request.POST, request.FILES)
        files = request.FILES.getlist('file') #field name in model
        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save(commit=False)
            feed_instance.user = user
            feed_instance.save()
            for f in files:
                file_instance = Document(file=f, feed=feed_instance)
                file_instance.save()
    else:
        form = Document()
        file_form = Document()
