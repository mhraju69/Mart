from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.createStore , name=""),
    path('<str:slug>/', views.store , name='store' )
]
