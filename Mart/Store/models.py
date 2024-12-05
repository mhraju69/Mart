from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()