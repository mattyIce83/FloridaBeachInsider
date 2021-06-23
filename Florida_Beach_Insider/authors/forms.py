from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'slug_name', 'active', 'title', 'bio', 'photo', 'email', 'facebook', 'twitter', 'instagram']


