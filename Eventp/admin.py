from django.contrib import admin
from . models import Eventform
from . models import calender
# Register your models here.
from .models import eventphoto
# Register your models here.
admin.site.register(eventphoto)
admin.site.register(Eventform)
admin.site.register(calender)