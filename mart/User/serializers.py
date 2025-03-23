from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','phone_number','address','birthdate','password','is_buyer','is_seller']
        extra_kwargs = {"password": {"write_only": True}}
        
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 200)
    class Meta:
        model = User
        fields = ['email', 'password']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name']
class changePassSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['new_password']
        
        
class resetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 200)
    class Meta:
        model = User
        fields = ['email']
        