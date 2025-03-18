from django.shortcuts import render,HttpResponse,get_object_or_404
from Store.models import *
from Products.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from User.serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DashboardAPI(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]  
    def user(self, request):
        user = request.user
        serializers = UserProfileSerializer(user)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def get_store(self, request):
        user = request.user
        store = Store.objects.filter(user=user)
        serializers = StoreSerializer(store, many=True)
        return Response({"user": user.email, "stores": serializers.data}, status=status.HTTP_200_OK)
    def get_product(self,request,store_slug):
        products = Products.objects.filter(store__slug=store_slug)
        serializers = ProductSerializer(products,many=True)
        return Response({"Product": serializers.data}, status=status.HTTP_200_OK)
        