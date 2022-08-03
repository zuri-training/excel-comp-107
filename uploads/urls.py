from django.urls import path
from . import views
from . import forms



app_name = 'upload'

urlpatterns = [
    path('', views.model_upload, name='model_upload'),
]


