from django.db import models


# Create your models here.

class Champion(models.Model):
    name = models.CharField(max_length=256, unique=True)
    hability_power = models.IntegerField()

