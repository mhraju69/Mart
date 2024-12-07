from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import storeSerializers

# Create your views here.

def store(request,slug):
    stores = Store.objects.filter(slug = slug)
    serializer = storeSerializers(stores,many = True)
    return JsonResponse(serializer.data,safe =  False)