from django.contrib import admin
from django import forms
from .models import Image

class ImageAdminForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'


class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm
    list_display = ['title', 'caption', 'image']
    readonly_fields = []

admin.site.register(Image, ImageAdmin)


