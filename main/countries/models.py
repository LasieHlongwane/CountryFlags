from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    population = models.PositiveIntegerField()
    capital = models.CharField(max_length=100)
    flag = models.URLField()

    def __str__(self):
        return self.name
