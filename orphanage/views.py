#this is homepage app
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, "index.html")
#this  fuction is to recieve web request and opens home  page of the website(web response)

   