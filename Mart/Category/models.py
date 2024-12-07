from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def url(self):
        return reverse('Category',kwargs=[self.slug])
    