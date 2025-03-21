from django.shortcuts import render
from django.views import View
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

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return User.objects.none()
        queryset = User.objects.filter(email=user.email)
        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        password = data.get("password")
        confirm_password = data.pop("confirm_password",None)
        if data.get('is_buyer','').strip().lower() == 'true' :
            data["is_seller"] = False
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


    def perform_update(self, serializer):
        
        data = self.request.data
        user =self.request.user
        if 'password' in data:
            current_password= data.get('password')
            new_password= data.get('new_password')
            confirm_password= data.get('confirm_password')
            
            if not new_password or not confirm_password :
                raise serializers.ValidationError({'error': 'new_password and confirm_password is requred'})
            
            if  new_password != confirm_password or not user.check_password(current_password):
                raise serializers.ValidationError({'error': 'Password mismatch'})
            
            serializer = changePassSerializer(data=data)
            
            if serializer.is_valid():
                print(serializer.validated_data)
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                
                return Response('Password Changed successfully',status=status.HTTP_200_OK)
        serializer.save()


def signup_view(request):
    return render(request, 'signup.html')  

class LoginView(APIView):
    
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            print(email,password,user)
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

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
