from django.db import models

# Create your models here.
class regformdthings(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    gender_choices = (('m', 'male'), ('f', 'female'), ('u', 'other'))
    gender = models.CharField(max_length=1, choices=gender_choices,null=True)
    age = models.IntegerField()
    pnumber = models.BigIntegerField()
    ntoys = models.CharField(max_length=50)
    nbooks = models.CharField(max_length=50) 
    nblankets = models.CharField(max_length=50) 
    dress =  models.CharField(max_length=50)
    clothes_choices = (('M', 'boy'),('F','girl'))
    cgender = models.CharField(max_length=1, choices=clothes_choices,null=True)
    others =  models.CharField(max_length=50)
    adress =  models.CharField(max_length=5000)
    landmark =  models.CharField(max_length=50)
    city =  models.CharField(max_length=50)
    district =  models.CharField(max_length=50)
#this "regformdthing" class in models.py represents tables or collection in our database for the form in donating things page of the website
class contactform(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
#this "contactform" class in models.py represents tables or collection in our database for the form in contact page of the website    