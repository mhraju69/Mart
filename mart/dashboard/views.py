from django.shortcuts import render,HttpResponse,get_object_or_404
from Store.models import *
from Products.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from User.serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class DashboardAPI(viewsets.ViewSet):
    pass
        