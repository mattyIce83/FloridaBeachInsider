"""************************************************************************
* ads.txt File Loader admin.py enables the appearance of the atfl app in
* the Django Admin Console.  The create_permissions call enables the app's
* individual permissions to appear in the User permissions / Available user 
* permissions thus allowing staff employees access w/o superuser status.    
************************************************************************"""
from django.contrib import admin
from .models import LoadTextFile

from django.contrib.auth.management import create_permissions
from django.apps import apps

admin.site.register(LoadTextFile)
create_permissions(apps.get_app_config('atfl'))
