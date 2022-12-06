from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class pay(models.Model):

     id = models.AutoField(primary_key=True)
     name=models.CharField(max_length=200)
     amount=models.BigIntegerField()
#this "pay" class in models.py represents tables or collection in our database for the payment  of the website

class financialreport(models.Model):
     fin=models.FileField(upload_to="pdfreports")
     fina=models.FileField(upload_to="pdfreports")
     year=models.CharField(max_length=50)
     yearf=models.CharField(max_length=50)
     yeara=models.CharField(max_length=50)
#this "financialreport" class in models.py represents tables or collection in our database for the pdf files in financial report page of the website     
#FileField is used for storing valid pdf files into the database. One can any type of image file in FileField.