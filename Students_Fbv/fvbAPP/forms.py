from django import forms
from fvbAPP.models import studentInfo

class studentList(forms.ModelForm):
    class Meta:
        model = studentInfo
        fields = '__all__'
