from django.shortcuts import render
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
    lookup_field = "slug"
    def get_queryset(self):
        queryset = Products.objects.filter(store__user = self.request.user)
        store_id = self.request.query_params.get('store')
        if store_id:
            queryset = Products.objects.filter(store = store_id)
        return queryset
    
    
    
    def create(self, request, *args, **kwargs):
        user =  request.user
        store_id = request.data.get('store')
        if not store_id:
            return Response({"error": "Store ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        store = get_object_or_404(Store,user=user,store=store_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(store=store)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
