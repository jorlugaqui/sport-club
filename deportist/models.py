from django.db import models
from schools.models import Club

# Create your models here.

class Deportist(models.Model):
    code = models.IntegerField(editable=False)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=60)
    birthdate = models.DateField()
    dni = models.CharField(max_length=255)
    club = models.ForeignKey(Club, null=True, on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        if not self.id:
            existing_records = Deportist.objects.filter(club=self.club)
            if existing_records.exists():
                self.code = f"{self.club.id}{self.code}"
                highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                self.code = highest_code + 1 if highest_code is not None else 1
                super().save(*args, **kwargs)
            else:

                highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                self.code = highest_code + 1 if highest_code is not None else 1
                self.code = f"{self.club.id}{self.code}"
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
        


    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {self.lastname}" 
