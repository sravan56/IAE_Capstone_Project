from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.
class gallery(models.Model):
    img=models.ImageField(upload_to="pictures",default="")
    info=models.CharField(max_length=50,default="")
#this "gallery" class in models.py represents tables or collection in our database for gallery page of our website
#ImageField is used for storing valid image files into the database. One can any type of image file in ImageField.
