from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.name} - {self.director}" 

class Period(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.availability}" 

class Coach(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.name} - {self.phonenumber}" 