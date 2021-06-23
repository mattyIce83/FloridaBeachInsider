"""***************************************************************
* views.py is the views file for fbi/atfl app. [ads.txt]
* index.html for blank page at 
*	http:// ...something... /atfl/
* LoadTextFile.html since the app's administrative interface will 
* not function without it.
***************************************************************"""
from django.shortcuts import render

def index(request):
    """" Calls file @ fbi/atfl/templates/atfl/index.html """
    return render(request, 'index.html', {})

def LoadTextFile(request):
	return render(request, 'LoadTextFile.html', {})
