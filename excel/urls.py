from django.urls import path
from excel import views as excel_views

app_name = "excel"  

urlpatterns = [
    
    path('', excel_views.home, name='home'),
    path('home', excel_views.home, name='home'),
    path('dashboard', excel_views.dashboard, name='dashboard'),
    path('posts', excel_views.Posts.as_view(), name='posts'),
    path('posts/<int:post_id>', excel_views.post_detail, name='post-detail'),

    path('posts/<int:post_id>/compare', excel_views.compare, name='compare'),

    path('multiple_files/', excel_views.FileFieldFormView.as_view(), name='multiple_files'),
    
    ]
