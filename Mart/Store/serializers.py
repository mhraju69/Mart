from rest_framework import serializers
from .models import*
class storeSerializers(serializers.ModelSerializer):
    class Meta:
        model= Store 
        
        fields = '__all__'