from django.db import models

# Create your models here.
class departmentMaster(models.Model):
    id = models.AutoField(primary_key = True)
    departmentname = models.CharField('Department Name', max_length=50)
