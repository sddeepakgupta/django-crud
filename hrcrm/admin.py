from django.contrib import admin
from hrcrm.models import * 
# Register your models here.
class departmentadmin(admin.ModelAdmin):
    pass
admin.site.register(departmentMaster, departmentadmin)