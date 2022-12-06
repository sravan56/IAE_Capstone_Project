# Create your models here.
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class eventphoto(models.Model):
    img=models.ImageField(upload_to="pictures",default="")
    info=models.CharField(max_length=50,default="")
#this "eventphoto" class in models.py represents tables or collection in our database for gallery page of our website
#ImageField is used for storing valid image files into the database. One can any type of image file in ImageField.

class Eventform(models.Model):

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    GChoices = (('M', 'Male'), ('F', 'Female'), ('O', 'Others'))
    Gender = models.CharField(max_length=1, choices=GChoices,null=True)
    Age=models.IntegerField()
    Phone=models.BigIntegerField()
    CCategory = (('F', 'Festival'), ('B', 'Birthday'), ('A', 'Anniversary'))
    Category = models.CharField(max_length=1, choices=CCategory,null=True)
    People=models.IntegerField()
    Event_Date = models.DateTimeField()
    Orphange_Home = (('2','Sri Alluri Yuvajana Seva Sangam'),('3','Mr Mani'),('4','Childrens Home'))
    Event_Celebrations=models.CharField(max_length=1,choices=Orphange_Home,null=True)
#this "Eventform" class in models.py represents tables or collection in our database for the form in event register page of the website    
class calender(models.Model):
    date=models.CharField(max_length=3)
    month=models.CharField(max_length=15)
    specialday=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    time=models.CharField(max_length=10)
#this "calender" class in models.py represents tables or collection in our database for the details in calender page of the website