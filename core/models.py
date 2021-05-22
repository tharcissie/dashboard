from django.db import models

# Create your models here.

class Amount(models.Model):
    price = models.PositiveIntegerField()
