from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Fam(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    cumple = models.DateField()
