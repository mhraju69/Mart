from django.urls import path,include
from . import views
urlpatterns = [
    path('categoty:<str:slug>', views.category , name='category')
]
