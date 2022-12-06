from django.contrib import admin
from .models import virat
# this virat class is for sponsor details form
from .models import payment
from .models import imgs


admin.site.register(virat)
admin.site.register(payment)

admin.site.register(imgs)


# Register your models here.
