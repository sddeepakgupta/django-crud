from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    instrument = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.first_name
