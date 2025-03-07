from django.shortcuts import render

from .serializers import *
from .models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
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
            user = seriallizer.save()
            user.set_password(password)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),
                        'access': str(refresh.access_token),'message': "User registration success"},status= status.HTTP_201_CREATED)
   

   
   
class LoginView(APIView):
    def post(self,request,format=None):
        serializer = SellerLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            print(user,email,password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'message': "Login success"
                    }, status=status.HTTP_200_OK)
            else:
                return Response({'error': "Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': "Invalid data"},status=status.HTTP_404_NOT_FOUND)





class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializers = UserProfileSerializer(request.user)
        
        return Response(serializers.data, status = status.HTTP_200_OK)

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
