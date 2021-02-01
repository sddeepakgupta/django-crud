from django.contrib import admin

# Register your models here.
from .models import Musician

class MusicianAdmin(admin.ModelAdmin):
    pass
admin.site.register(Musician, MusicianAdmin)