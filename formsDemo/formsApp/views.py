from django.shortcuts import render
from . import forms


def UserRegistrationView(request):
    form = forms.userRegistration()

    if request.method == 'POST':
        form = forms.userRegistration(request.POST)

        if form.is_valid():
            print('Success', form.cleaned_data)

    return render (request,'formsApp/userform.html',{'form':form})