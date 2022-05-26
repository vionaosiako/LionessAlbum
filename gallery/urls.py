from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('viewPhoto/<str:pk>', views.viewPhoto, name='viewPhoto'),
    path('addGallery', views.addGallery, name='addGallery'),
    
]