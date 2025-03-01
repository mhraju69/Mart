from django.shortcuts import render

from .serializers import SellerSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password

# Create your views here.

class SellerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SellerSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        password = data.get("password")
        confirm_password = data.get("confirm_password",None)
        
        if password != confirm_password :
            return Response({'error': "Password missmatch"},status= status.HTTP_308_PERMANENT_REDIRECT)
        
        if User.objects.filter(email=data.get("email")).exists():
            return Response({'error': "Email already exist"},status= status.HTTP_207_MULTI_STATUS)
        
        seriallizer = self.get_serializer(data=data)
        
        if seriallizer.is_valid(raise_exception=True):
            seriallizer.save( password = make_password(password))
        
            return Response({'message': "User registration success"},status= status.HTTP_201_CREATED)
    
