from rest_framework import serializers

from .models import *

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer()
    class Meta:
        model = Cart
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        