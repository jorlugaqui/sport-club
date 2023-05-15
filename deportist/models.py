from django.db import models

# Create your models here.
class Deportist(models.Model):
    registrationcode = models.IntegerField(max_length=3)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=60)
    birthdate = models.DateField()
    dni = models.CharField(max_length=255)
