from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from courseApp.models import course
from django.urls import reverse_lazy

class courseListView(ListView):
    model = course

class courseDetailView(DetailView):
    model = course

class courseCreateView(CreateView):
    model = course
    fields =('name', 'description', 'instructor', 'rating')

class courseUpdateView(UpdateView):
    model = course
    fields =('name', 'description', 'instructor', 'rating')

class courseDeleteView(DeleteView):
    model = course
    success_url = reverse_lazy('courselist')