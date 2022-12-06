from django.shortcuts import render
from .models import gallery
# Create your views here.
def galery(request):
    photo=gallery.objects.all()
    return render(request,'gallery.html',{'photo':photo})
#this view fuction is to recieve web request from user and redirect to the gallery of the website(web response)
# this is for gallery page     