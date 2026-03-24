from django.shortcuts import render, redirect
from clinicalApp.models import Patient, ClinicalData
from clinicalApp.forms import PatientForm, ClinicalDataForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    fields = ('name','age')
    success_url = reverse_lazy('Index')

class PatientUpdateView(UpdateView):
    model = Patient
    fields = ('name','age')
    success_url = reverse_lazy('Index')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('Index')

def addData(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalApp/clinicaldata.html',{'form':form,'patient':patient})


