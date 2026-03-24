from django import forms
from mforms.models import formCreation

class modelFormCreation(forms.ModelForm):
    class Meta:
        model = formCreation
        fields = '__all__'
