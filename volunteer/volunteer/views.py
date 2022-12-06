from django.shortcuts import render
from .models import volunteer
from django.http import HttpResponse
# Create your views here.
def  p2(request):
    return render(request,"p2.html")


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
        return HttpResponse("<h1>data succesgully saved</h1>")
    return render(request,"volregistration.html")

def  ragava(request):
    return render(request,"p3.html")