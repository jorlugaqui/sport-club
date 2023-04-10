from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name