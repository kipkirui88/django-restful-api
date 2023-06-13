from django.db import models

# Create your models here.
class students(models.Model):
    adm = models.IntegerField()
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
