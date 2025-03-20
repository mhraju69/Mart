from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from .serializers import *

# Create your views here.

class CartViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    lookup_field = 'product_slug'
    serializer_class = CartSerializer
    def get_cartitems(self,request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request,product_slug=None,*args, **kwargs):
        user = request.user
        cart , created = Cart.objects.get_or_create(user=user)
        product = get_object_or_404(Products,product_slug=product_slug)
        cartitem , created = CartItem.objects.get_or_create(cart=cart ,product=product)

        if not created :
            cartitem.quantity += 1
            cartitem.save()
        serializer = CartItemSerializer(cartitem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
            