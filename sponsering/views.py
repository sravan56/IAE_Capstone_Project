from django.shortcuts import render
from .models import virat
# this virat class is for sponsor details form 
from .models import payment
from .models import imgs
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def sponsor(request):
    return render(request,"sponsoredpage.html")
#"sponsor" fuction is to recieve web request from user and redirect to the sponsor main page of the website(web response)
# this is for sponsor main page     
def sponsored(request):
    if request.method=="POST":

        fn=request.POST["fname"]
        ln=request.POST["lname"]
        g=request.POST["gender"]
        em=request.POST["email"]
        ph=request.POST["phone"]
        re=request.POST["Role"]
        amt=request.POST["amount"]
        add=request.POST["address"]
        mes=request.POST["message"]
        data=virat(fname=fn,lname=ln,gender=g,email=em,phone=ph,Role= re,amount=amt,address=add,message=mes)
        data.save()
        return redirect("spnsrpayment")
        return HttpResponse("<h1> Successful:)</h1>")
        return render(request,"payment.html")

    return render(request,"sponsored.html")
#this "sponsored" function is for form in sponsor page which seeks the basics details of the sponsor
def sponsoring(request):
    
    return render(request,'sponsorship.html')
#"sponsoring"  fuction is to recieve web request from user and redirect to the sponsoring details page of the website(web response)
def img(request):

    pics=imgs.objects.all()
    return render(request,'images.html',{'pics':pics})        
#this "imgs" fuction is to recieve web request from user and redirect to the children waiting for sponsor of the website(web response)     
def adoption(request):
    return render(request,"adopt.html")
#this "adoption" fuction is to recieve web request from user and redirect to the adoption page of the website(web response)
def spnsrpayment(request):
    if request.method=="POST":

        
        cardname=request.POST["name"]
        cardnumber=request.POST["card"]
        data=payment(name=cardname,card=cardnumber)
        data.save()
        return HttpResponse("<h1>  Payment Successful:)</h1>")
#this "spnsrpayment" function is for payment  page which is for payment

        return redirect("sponsor")


    return render(request,"payment.html")