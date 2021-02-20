from django.core import validators
from django import forms
from .models import Musician, productMaster
from django.core.files.uploadedfile import SimpleUploadedFile
from djrichtextfield.widgets import RichTextWidget

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
class productMasterForm(forms.ModelForm):
    class Meta:
        model = productMaster
        fields = '__all__'
        widgets = {
           'productName':forms.TextInput(attrs={'class':'form-control'}),
           'productType':forms.Select(attrs={'class':'form-control'}),
           'productCategories':forms.Select(attrs={'class':'form-control'}),
           'productPrize':forms.TextInput(attrs={'class':'form-control'}),
           'productReleaseDate':forms.DateInput(attrs={'class':'form-control'}),
           'productProductImage':forms.ClearableFileInput(attrs={'multiple': True, 'class':'form-control'}), 
           'productDescription':forms.CharField(widget=RichTextWidget()),
           'active':forms.Select(attrs={'class':'form-control'}), 
        }        

    