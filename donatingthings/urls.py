from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    
    path("dthings", views.dthings, name="dthings"),
path("dtreform", views.dtreform, name="dtreform"),
path("contact", views.contact, name="contact"),

]