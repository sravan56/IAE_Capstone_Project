from django.urls import path

from . import views

urlpatterns = [
    path("p2", views.p2, name="p2"),
   path("vl", views.vl, name="vl"),
   path("ragava",views.ragava, name='ragava'),

]