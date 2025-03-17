from django.shortcuts import render,HttpResponse
from Store.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Store.serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DashboardAPI(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user  
        stores = Store.objects.filter(user=user)
        serializer = StoreSerializer(stores, many=True)
        return Response({"user": user.email, "stores": serializer.data}, status=status.HTTP_200_OK)