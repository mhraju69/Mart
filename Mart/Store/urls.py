from django.urls import path,include
from . import views
urlpatterns = [
    path('<str:slug>/', views.store , name='store' )
]
