from django.shortcuts import render


def home(request):
    # documents = Document.objects.all()
    return render(request, 'excel/home.html')
