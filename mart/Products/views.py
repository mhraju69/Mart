from django.shortcuts import render,get_object_or_404
from .serializers import ProductSerializer
from .models import Products
from Store.models import *
from rest_framework import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class productViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    def get_product(self, request,store_slug=None,product_slug=None):
        user = request.user
        product = Products.objects.filter(store__user=user)
        if store_slug:
            product = Products.objects.filter(store__user=user , store__slug = store_slug)
            serializers = ProductSerializer(product, many=True)
        if store_slug and product_slug:
            product = get_object_or_404(Products,store__user=user,slug=product_slug,store__slug = store_slug)
            serializers = ProductSerializer(product)
        
        return Response({"user": user.email, "products": serializers.data}, status=status.HTTP_200_OK)

    def create(self, request,store_slug=None, *args, **kwargs):
        user =  request.user
        store = get_object_or_404(Store,user=user,slug=store_slug)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(store=store)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
