from django import forms
from courseList.models import course

class courseUpdate(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'