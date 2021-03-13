from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.
from .models import *

class MusicianAdmin(admin.ModelAdmin):
    pass
admin.site.register(Musician, MusicianAdmin)

class productMasterForm(forms.ModelForm):
    productProductImage = forms.CharField(widget=CKEditorWidget())
    productDescription = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = productMaster
        fields = '__all__'
class productAdmin(admin.ModelAdmin):
    pass
admin.site.register(productType, productAdmin)
admin.site.register(productCategories, productAdmin)
admin.site.register(productMaster, productAdmin)
admin.site.register(bookMaster, productAdmin)