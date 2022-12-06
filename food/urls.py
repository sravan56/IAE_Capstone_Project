from django.urls import path

from . import views

urlpatterns = [path("sfp", views.sfp, name="sfp"),
path("moreinfo", views.moreinfo, name="moreinfo"),
path("operations", views.operations, name="operations"),
path("registerform", views.registerform, name="registerform"),
]