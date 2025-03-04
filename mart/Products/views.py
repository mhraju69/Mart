from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Products
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class productViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
