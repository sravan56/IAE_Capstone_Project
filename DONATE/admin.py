from django.contrib import admin
from . models import pay
from . models import financialreport


# Register your models here.
admin.site.register(pay)
admin.site.register(financialreport)
