from django.db import models
from Sellers.models import User
# Create your models here.

class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='store_images',blank=True, null=True)

    def __str__(self):
        return self.name
