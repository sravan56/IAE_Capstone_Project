from django.urls import path

from . import views


urlpatterns = [

    path("eve", views.eve, name="eve"),
    path("calen", views.calen, name="calen"),
    path("regform", views.regform, name="regform"),
    path("gal", views.gal, name="gal"),


]