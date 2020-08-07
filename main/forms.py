from django import forms
from .models import Jasoseol

class JssFormm(forms.ModelForm):
    
    class Meta:
        model = Jasoseol
        fields = ("title",'content',)
