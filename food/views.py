from django.shortcuts import render
from django.shortcuts import redirect
from . models import foodregdetails
from django.http import HttpResponse
# Create your views here.
def  sfp(request):
     return render(request, "surplusfoodpage.html")
#this  fuction is to recieve web request from user and redirect to the surplus food page of the website(web response)
def  moreinfo(request):
     return render(request, "moreinfo.html")
#this  fuction is to recieve web request from user and redirect to the more info(guide lines for donating food) page of the website(web response)
def  operations(request):
     return render(request, "operations.html")
#this  fuction is to recieve web request from user and redirect to the operations page(howfood is circulated) of the website(web response)
def registerform(request):
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        ph = request.POST["phone"]
        f1 = request.POST["food1"]
        f2 = request.POST["food2"]
        fd = request.POST["fooddate"]
        fq = request.POST["foodQuantity"]
        fp = request.POST["foodpack"]
        lc = request.POST["locality"]
        ct= request.POST["city"]
        dt= request.POST["district"]
        st= request.POST["state"]
        pn= request.POST["pin"]
        data = foodregdetails(fname=fn,lname=ln,email=em,phone=ph,food1=f1,food2=f2,fooddate=fd,foodQuantity=fq,foodpack=fp,locality=lc,city=ct,district=dt,state=st,pin=pn)
        data.save()
#this "registerform" function is for form in surplus food form page which seeks the basics details for donating surplus food           
        return HttpResponse("<h1>data succesfully saved</h1>")
        return redirect("sfp")
    return render(request,"foodregister.html")