from django.db import models
from User.models import User
from Products.models import *

# Create your models here.

class Cart(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    
    