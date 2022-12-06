from django.db import models

# Create your models here.

class foodregdetails(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone =models.BigIntegerField()
    FOOD_CHOICES = (('M', 'veg'), ('F', 'nonveg'), ('U', 'both'))
    food1 = models.CharField(max_length=1, choices=FOOD_CHOICES,null=True)
    FOODSTATE_CHOICES = (('FRO', 'frozen'), ('FRE', 'fresh'), ('COOK', 'cooked'))
    food2 = models.CharField(max_length=4, choices=FOODSTATE_CHOICES,null=True)
    fooddate = models.DateTimeField(auto_now=False, auto_now_add=False)
    foodQuantity = models.IntegerField(null=True)
    FOOD_PACK = (('L', 'loose'), ('P', 'packed'))
    foodpack = models.CharField(max_length=1, choices=FOOD_PACK,null=True)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin= models.CharField(max_length=10)
#this "foodregdetails" class in models.py represents tables or collection in our database for the form in the surplus food page of the website


