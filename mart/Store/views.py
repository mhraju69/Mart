from django.shortcuts import render
from .serializers import StoreSerializer
from .models import Store
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class storeViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)