from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework import status
from rest_framework.response import Response
from .serializers import storeSerializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def store(request,slug):
    stores = Store.objects.filter(slug = slug)
    serializer = storeSerializers(stores,many = True)
    return JsonResponse(serializer.data,safe =  False)

def createStore(request):
    if request.method == 'POST':
            serializer = storeSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status = status.HTTP_201_CREATED)  
            return Response (serializer.errors,status= status.HTTP_400_BAD_REQUEST)