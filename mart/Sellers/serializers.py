from rest_framework import serializers

from .models import User

class SellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name','phone_number','address','birthdate','password','is_buyer','is_seller']
        extra_kwargs = {"password": {"write_only": True}}
        
class SellerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 200)
    class Meta:
        model = User
        fields = ['email', 'password']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name','last_name']
       