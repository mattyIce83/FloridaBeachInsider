from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Filter
from .forms import FilterForm


class FilterListView(ListView):
    model = Filter


class FilterCreateView(CreateView):
    model = Filter
    form_class = FilterForm


class FilterDetailView(DetailView):
    model = Filter


class FilterUpdateView(UpdateView):
    model = Filter
    form_class = FilterForm

