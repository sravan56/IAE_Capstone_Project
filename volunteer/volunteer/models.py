
from django.db import models

# Create your models here.
class volunteer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    Gender_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    gender = models.CharField(max_length=7, choices=Gender_CHOICES)
    Availability_CHOICES = (('WD', 'weekdays'), ('WE', 'weekends'), ('B', 'both'),('V','varies'))
    availability = models.CharField(max_length=2, choices=Availability_CHOICES)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    role = models.CharField(max_length=400)
    address = models.CharField(max_length=50)
    message = models.CharField(max_length=50)