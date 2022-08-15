from django.urls import path
from . import views

app_name = "users"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home", views.homepage, name="homepage"),
    path("register", views.register_request, name='register'),
    path("login", views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path("success", views.register_success, name="success"),
    path("profile", views.profile, name="profile"),
]
