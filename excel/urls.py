from django.urls import path
from . import views

app_name = "excel"   


urlpatterns = [
    path("", views.home, name="home"),

]
