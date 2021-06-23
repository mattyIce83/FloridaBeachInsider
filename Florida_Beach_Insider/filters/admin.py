from django.contrib import admin
from django import forms
from .models import Filter

class FilterAdminForm(forms.ModelForm):

    class Meta:
        model = Filter
        fields = '__all__'


class FilterAdmin(admin.ModelAdmin):
    form = FilterAdminForm
    list_display = ['name', 'active']
    readonly_fields = []

admin.site.register(Filter, FilterAdmin)


