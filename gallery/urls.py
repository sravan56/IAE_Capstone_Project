from django.urls import path
from . import views

urlpatterns = [path("galery", views.galery, name="galery"),
]