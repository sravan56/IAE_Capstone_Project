from django.shortcuts import render
from django.http import HttpResponse
from . models import pay
from . models import financialreport
# Create your views here.
def  dont(request):
     return render(request, "donate.html")

#this  fuction is to recieve web request from user and redirect to the donate page of the website(web response)
def  finreprt(request):
     
     return render(request,'finrep.html')

#this  fuction is to recieve web request from user and redirect to the financial report page of the website(web response)     
def payment(request):
    if request.method=="POST":
        
        cardname=request.POST["name"]
        damount=request.POST["amount"]
        data=pay(name=cardname,amount=damount)
        data.save()
        return HttpResponse("<h1>submitted succesfully</h1>")
        
     
        
#this "dtreform" function is for form in donating things form page which seeks the payment details of sponsors
    return render(request,"payments.html")
def finpdfs(request):

     finr=financialreport.objects.all()
     return render(request,'finrepdf.html',{'finr':finr})    

#this  "finpdfs" fuction is to recieve web request from user and redirect to the financial report page of the website(web response)