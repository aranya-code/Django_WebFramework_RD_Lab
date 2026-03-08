from django import forms
from movieList.models import movie

class movieCreation(forms.ModelForm):
    # Creating form out of the model movie
    class Meta:
        model = movie
        fields = '__all__'
        

