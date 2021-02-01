from django.core import validators
from django import forms
from .models import Musician

# ####model froms data define
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'instrument']
        widgets = {
           'first_name':forms.TextInput(attrs={'class':'form-control'}),
           'last_name':forms.TextInput(attrs={'class':'form-control'}),
           'instrument':forms.TextInput(attrs={'class':'form-control'}), 
        }

    