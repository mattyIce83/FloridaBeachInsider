from django.contrib import admin
from django import forms
from .models import Author

class AuthorAdminForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ['first_name', 'last_name', 'slug_name', 'active', 'title', 'bio', 'photo', 'email', 'facebook', 'twitter', 'instagram']
    readonly_fields = []

admin.site.register(Author, AuthorAdmin)


