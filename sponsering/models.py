from django.db import models

# Create your models here.
# this virat class is for sponsor details form
class virat(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50) 
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES,null=True)
    email=models.EmailField(max_length=50)
    phone=models.BigIntegerField()
    Role=models.CharField(max_length=200) 
    amount=models.IntegerField(default=0)
    address=models.CharField(max_length=500)
    message=models.CharField(max_length=200)
#this "virat" class in models.py represents tables or collection in our database for the form in sponsor page of the website

class imgs(models.Model):
    

    img=models.ImageField(upload_to="pictures",default="")
    name=models.CharField(max_length=50,default="")
    age=models.CharField(max_length=50,default="")    
#this "imgs" class in models.py represents tables or collection in our database for children waiting for sponsor of the website
    
class payment(models.Model):

    name=models.CharField(max_length=200)
    card=models.BigIntegerField()
#this "payment" class in models.py represents tables or collection in our database for the  payment page in sponsor page of the website    