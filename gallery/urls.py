from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('upload_image/', views.upload_image, name='upload_image'), 
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('like/<int:image_id>/', views.like_image, name='like_image'),
    path('dislike/<int:image_id>/', views.dislike_image, name='dislike_image'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
