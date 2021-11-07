from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name='home'),
    path("crime_infanticide", views.crime_infanticide ,name='crime_infanticide')
    

]