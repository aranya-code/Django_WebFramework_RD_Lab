from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from CBVApp.models import studentInfo
from django.urls import reverse_lazy

class studentInfoView(ListView):
    model = studentInfo
    # default template name should be studentinfo_list.html
    # default context_object_name should be studentinfo_list


class studentDetailsView(DetailView):
    model = studentInfo
    # default template name should be studentinfo_detail.html
    # default context_object_name should be studentinfo

class studentCreateView(CreateView):
    model = studentInfo
    fields = '__all__'

class studentUpdateView(UpdateView):
    model = studentInfo
    fields = ('name','score')

class studentDeleteView(DeleteView):
    model = studentInfo
    success_url = reverse_lazy ('student')