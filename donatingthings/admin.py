from django.contrib import admin
from . models import contactform
# Register your models here.
from . models import regformdthings
# Register your models here.
admin.site.register(regformdthings)
admin.site.register(contactform)