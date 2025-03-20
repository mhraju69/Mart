from rest_framework import serializers
from .models import *
from Products.serializers import *

        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    class Meta:
        model = CartItem
        exclude = ['cart']
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True,source='cartitem_set',read_only=True)
    class Meta:
        model = Cart
        exclude = ['user']

        