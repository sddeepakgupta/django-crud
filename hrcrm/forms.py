from django.core import validators
from django import forms
from hrcrm.models import *
# Make Your forms here
class departmentForm(forms.ModelForm):
    class Meta:
        model = departmentMaster
        fields = '__all__'
        widgets = {
            'departmentname':forms.TextInput(attrs('class':'form-control'))
        }

