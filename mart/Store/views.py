from django.shortcuts import render,get_list_or_404
from .serializers import StoreSerializer
from .models import Store
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class storeViewset(viewsets.ModelViewSet):
    
    
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]
    def get_store(self, request,store_slug=None):
        user = request.user
        store = Store.objects.filter(user=user)
        if store_slug:
            store = get_list_or_404(Store,user=user,slug=store_slug)
        serializers = StoreSerializer(store, many=True)
        return Response({"user": user.email, "stores": serializers.data}, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
