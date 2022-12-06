"""ORPHANAGE_MANAGEMENT_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('orphanage.urls')),
    path('food/', include('food.urls')),
    
    
    path('Eventp/', include('Eventp.urls')),
     path('volunteer/', include('volunteer.urls')),
     path('donatingthings/',include('donatingthings.urls')),
     path('DONATE/',include('DONATE.urls')),
    
     path('sponsering/',include('sponsering.urls')),
     path('gallery/',include('gallery.urls')),
    
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
   
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#This describes Django's file access APIs for files such as those uploaded by a user. If you want to handle “static files” (JS, CSS, etc.),
#  see Managing static files (e.g. images, JavaScript, CSS). ... By default, Django stores files locally, using the MEDIA_ROOT and MEDIA_URL
#  settings
