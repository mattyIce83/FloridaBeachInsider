"""***************************************************************************************
* urls.py is the local urls.py file for the Beaches atfl app. [ads.txt]  This 
* file is "included" in opt/django-projects/beaches-cms/   politifact/urls.py
* NOTE: atlf app dependent on etc/nginx/path_2_configuration_file
* configured for an nginx level redirect, thus requests to FloridaBeachInsider.com/ads.txt
* are redirected to http://static.politifact.com.s3.amazonaws.com/ads.txt .
* The files models.py, root level urls.py, app level urls.py, vies.py, and 
* admin.py control the app's behavior in the Django adminstrative console.
* Include path to this file from site's main urls.py = "../atfl/urls.py" (no quotes).
***************************************************************************************"""
from django.conf.urls import url
from atfl.views import index, LoadTextFile

app_name = 'atfl'

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^TextFileUploader/$', LoadTextFile, name='LoadTextFile'),
]
