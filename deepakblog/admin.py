from django.contrib import admin

# Register your models here.
from .models import *

class MusicianAdmin(admin.ModelAdmin):
    pass
admin.site.register(Musician, MusicianAdmin)

class productAdmin(admin.ModelAdmin):
    pass
admin.site.register(productType, productAdmin)
admin.site.register(productCategories, productAdmin)
admin.site.register(productMaster, productAdmin)