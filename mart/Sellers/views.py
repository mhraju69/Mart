from django.shortcuts import render

from .serializers import SellerSerializer, SellerLoginSerializer
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
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
        
        if User.objects.filter(username=data.get("username")).exists():
            return Response({'error': "Email already exist"},status= status.HTTP_207_MULTI_STATUS)
        
        seriallizer = self.get_serializer(data=data)
        
        if seriallizer.is_valid(raise_exception=True):
            seriallizer.save( password = make_password(password))
        
            return Response({'message': "User registration success"},status= status.HTTP_201_CREATED)
   
   
   
   
class LoginView(APIView):
    def post(self,request,format=None):
        serializer = SellerLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = User.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'message': "Login success"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': "Invalid data"},status=status.HTTP_404_NOT_FOUND)
        
           
       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
