from django.shortcuts import render
from .models import volunteer
from django.http import HttpResponse
# Create your views here.
def  p2(request):
    return render(request,"p2.html")
#this "p2" fuction is to recieve web request from user and redirect to the volunteer page of the website(web response)  

def  vl(request):
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        gender = request.POST["gender"]
        avl = request.POST["availability"]
        email = request.POST["email"]
        ph = request.POST["phone"]
        role = request.POST["role"]
        adr = request.POST["address"]
        msg = request.POST["message"]
        volunteer_data=volunteer(fname=fn,lname=ln,gender=gender,availability=avl,email=email,phone=ph,role=role,address=adr,message=msg)
        volunteer_data.save()
        return HttpResponse("<h1>data succesfully saved</h1>")
    return render(request,"volregistration.html")
#this "vl" function is for volunteer form page which seeks the basic details of users about the website
def  ragava(request):
    return render(request,"p3.html")
#this "ragava" fuction is to recieve web request from user and redirect to the life as a volunteer page of the website(web response)    