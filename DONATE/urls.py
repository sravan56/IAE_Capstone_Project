
from django.urls import path
from . import views

urlpatterns = [path("dont", views.dont, name="dont"),
path("finreprt", views. finreprt, name="finreprt"),
path("payment",views.payment,name="payment"),
path("finpdfs",views.finpdfs,name="finpdfs"),
]