from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):
    
    class Meta:
        model = Jasoseol
        fields = ("title",'content',)
