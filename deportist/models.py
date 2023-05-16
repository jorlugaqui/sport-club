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
    club_id = models.ForeignKey(Club, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.code = f"{self.club_id.id}{self.code}"
        if not self.id:
            highest_code = Deportist.objects.aggregate(models.Max('code'))['code__max']
            self.code = highest_code + 1 if highest_code is not None else 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.name} - {self.lastname}" 
