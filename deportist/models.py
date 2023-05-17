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
            existing_records = Deportist.objects.filter(club=self.club).order_by('-code')[:1]
            if existing_records.exists():
                existing_code = existing_records[0].code
                if existing_code != self.id:
                    self.code = str(existing_code + 1).zfill(5)
                    super().save(*args, **kwargs)
                else:
                    if existing_records[0].club != self.club:
                        highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                        self.code = str(highest_code + 1).zfill(5) if highest_code is not None else '00001'
                        super().save(*args, **kwargs)
            else:
                highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                self.code = str(highest_code + 1).zfill(5) if highest_code is not None else '00001'
                self.code = f"{self.club.id}{self.code}"
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {self.lastname}"
