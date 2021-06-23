from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Author
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm


class AuthorDetailView(DetailView):
    model = Author


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm

