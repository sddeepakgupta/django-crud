from django.core import validators
from django import forms
from .models import Musician, productMaster, bookMaster
# from django.core.files.uploadedfile import SimpleUploadedFile
from ckeditor.widgets import CKEditorWidget

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
        #    'productProductImage':forms.CharField(widget=CKEditorWidget()), 
           'productDescription':forms.CharField(widget=CKEditorWidget()),
           'active':forms.Select(attrs={'class':'form-control'}), 
        } 
#  Book Master Details
class bookMasterForms(forms.ModelForm):
    class Meta:
        model = bookMaster
        fields = '__all__'
        widgets = {
           'bookName':forms.TextInput(attrs={'class':'form-control'}),
           'bookDescription':forms.CharField(widget=CKEditorWidget()), 
        }

    