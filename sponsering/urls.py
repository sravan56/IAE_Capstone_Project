from django.urls import path

from . import views

urlpatterns = [path("sponsor", views.sponsor, name="sponsor"),
path("sponsored", views.sponsored, name="sponsored"),
path("sponsoring", views.sponsoring, name="sponsoring"),
path("adoption", views.adoption, name="adoption"),
path("spnsrpayment", views.spnsrpayment, name="spnsrpayment"),
path("img", views.img, name="img"),

]