"""*********************************************************************
* models.py is the model definition file for the atfl app. [ads.txt]
* Using the Django Administration console, authorized users can upload
* ads.txt files to the Django project fbi root.
* The app assumes usage of s3.botoStorage and overwrites the ads.txt
* file directly to http://static.politifact.com.s3.amazonaws.com/ads.txt
* with file name and size validation included.
*********************************************************************"""
from django.core.exceptions import ValidationError
from django.db import models
import os

helpText = "Click 'Choose File' to select an ads.txt file from your local hard drive. The file on your hard drive MUST be named 'ads.txt' and be less than 100KB in size."

def validateFileName(value):
    """ Validate uploaded file name is ads.txt. Note: validateFileName built in this manner because
        calling os.path.basename() is not functioning in our environment. """
    extension = str(os.path.splitext(value.name)[1])
    thePath = str(os.path.splitext(value.name)[0])
    fullPath = str(thePath + extension)
    testFileName = str(os.path.basename(fullPath))
    validFileName = ['ads.txt']
    if not testFileName in validFileName:
        raise ValidationError(u'File Naming Error! You may only upload files named \'ads.txt\'')

def validateFileSize(value):
    """ Validate file size - limited here to 100KB """
    fileSize = value.file.size
    allowedSize = 100000
    if fileSize > allowedSize:
        raise ValidationError(u'Size Error! You may not upload files greater than 100KB.')

class LoadTextFile(models.Model):
    """ Pre-populates FileName field in Admin console and validates/uploads the ads.txt file. """
    fileName = models.CharField(max_length=7, default='ads.txt', help_text = helpText)
    file = models.FileField(validators=[validateFileName, validateFileSize], null=True)