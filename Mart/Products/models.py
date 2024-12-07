from django.db import models
from Store.models import *
# Create your models here.

class Products(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    details = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    