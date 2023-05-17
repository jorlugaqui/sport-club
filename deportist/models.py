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
            existing_records = Deportist.objects.filter(club=self.club).order_by('-code')[:1] #se filtra y se limita a 1
            if existing_records.exists():
                existing_code = existing_records[0].code
                if existing_code != self.id: #se compara si es diferente de self.id
                    self.code = str(existing_code + 1).zfill(5) #al ser diferente se le suma 1 al código y guarda
                    super().save(*args, **kwargs)
                else: #si son diferentes
                    if existing_records[0].club != self.club: #se valida el club
                        highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                        self.code = str(highest_code + 1).zfill(5) if highest_code is not None else '00001'
                        super().save(*args, **kwargs)
            else: #si no existe ningún dato guardado
                highest_code = Deportist.objects.filter(club=self.club).aggregate(models.Max('code'))['code__max']
                self.code = str(highest_code + 1).zfill(5) if highest_code is not None else '00001'
                self.code = f"{self.club.id}{self.code}"
                super().save(*args, **kwargs)
        else: #si no es ninguna de las anteriores no se hace nada
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {self.lastname}"
