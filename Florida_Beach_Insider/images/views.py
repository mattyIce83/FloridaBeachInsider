from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Image
from .forms import ImageForm


class ImageListView(ListView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm


class ImageDetailView(DetailView):
    model = Image


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm

