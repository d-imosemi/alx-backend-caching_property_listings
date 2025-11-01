# properties/urls.py

from django.urls import path
from properties import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
]