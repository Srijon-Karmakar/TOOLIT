from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube, name='youtube'),  # YouTube page
    path('facebook/', views.facebook, name='facebook'),  # Facebook page
    path('instagram/', views.instagram, name='instagram'),  # Instagram page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Add this line for the contact page  # Optional: Add services page if needed
  
]
