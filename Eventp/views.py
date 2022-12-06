from django.shortcuts import render
from . models import Eventform
from . models import eventphoto
from . models import calender
from django.http import HttpResponse
# Create your views here.
def  eve(request):
     return render(request, "Event.html")
#this "eve" fuction is to recieve web request from user and redirect to the event page of the website(web response)
# this is for  event event page
def  calen(request):
     cal=calender.objects.all()
     return render(request, "Calender.html",{'cal':cal})
#this "calen" fuction is to recieve web request from user and redirect to the event calender of the website(web response)
# this is for  event calender page
def  regform(request):
     if request.method =="POST":
         f1=request.POST["first_name"]
         l1=request.POST["last_name"]
         e=request.POST["email"]
         ge=request.POST["Gender"]
         a=request.POST["Age"]
         ph=request.POST["Phone"]
         CC=request.POST["Category"]
         Pe=request.POST["People"]
         EvD=request.POST["Event_Date"]
         OH=request.POST["Event_Celebrations"]
         data=Eventform(first_name=f1,last_name=l1,email=e,Gender=ge,Age=a,Phone=ph,Category=CC,People=Pe,Event_Date=EvD,Event_Celebrations=OH)
         data.save()
#this "regform" function is for event form page which seeks the basic details of users regarding event celebrations             
         return HttpResponse("<h1>datasaved successfully</h1>")          
     return render(request, "HELP.html")
#this  fuction is to recieve web request from user and redirect to the event form page of the website(web response)          
def  gal(request):
     photo=eventphoto.objects.all()
     return render(request,'newone.html',{'photo':photo}) 
#this "gal" fuction is to recieve web request from user and redirect to the event gallery of the website(web response)
# this is for  event gallery page          