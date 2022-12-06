from django.shortcuts import render
from django.http import HttpResponse
from . models import regformdthings
from . models import contactform
# Create your views here.

# Create your views here.
def contact(request):
     if request.method=='POST':
          name=request.POST['name']
          ph=request.POST['phone']
          emailid=request.POST['email']
          sub=request.POST['subject']
          mes=request.POST['message']
          datac = contactform(name=name,phone=ph,email=emailid,subject=sub,message=mes)
          datac.save()
          return HttpResponse("<h1>submitted succesfully</h1>")
#this "contact" function is for contact form page which seeks the queries of users about the website

     return render(request, "contactus.html")

def  dthings(request):
     return render(request, "donatingthings.html")
#this  fuction is to recieve web request from user and redirect to the donating things page of the website(web response)
def  dtreform(request):
     if request.method == 'POST':
       f1 = request.POST['fname']
       l1 = request.POST['lname']
       e1 = request.POST['email']
       ge = request.POST['gender']
       a1 = request.POST['age']
       p1 = request.POST['pnumber'] 
       nt = request.POST['ntoys']
       b1 = request.POST['nbooks']
       nb = request.POST['nblankets']
       dr = request.POST['dress']
       cg = request.POST['cgender']
       ot = request.POST['others']
       ad = request.POST['adress']
       la = request.POST['landmark']
       ci = request.POST['city']
       di = request.POST['district']
       data = regformdthings(fname=f1, lname=l1, email=e1, gender=ge, age=a1, pnumber=p1, ntoys=nt, nbooks=b1, nblankets=nb, dress=dr, cgender=cg, others=ot, adress=ad,landmark=la,city=ci,district=di)
       data.save()
       return HttpResponse("<h1>submitted successfully</h1>")
     return render(request, "dtregisterform.html")
#this "dtreform" function is for form in donating things form page which seeks the basics details for donating things     


