
from django.contrib import admin
from django.urls import path,include
from User.views import*
from Store.views import*
from Products.views import*
from dashboard.views import*
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
routers = DefaultRouter()
routers.register(r"user", UserViewSet,basename="user")
routers.register(r"stores", storeViewset ,basename="stores")
routers.register(r"products", productViewset ,basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(routers.urls)),
    path('api/login/',LoginView.as_view(),name="login_api"),
    path('dashboard/',DashboardAPI.as_view({'get':'user'}),name='profile'),
    path('dashboard/store/',DashboardAPI.as_view({'get':'get_store'}),name='store_by_user'),
    path('dashboard/store:<slug:slug>/',DashboardAPI.as_view({'get':'get_product'}),name="product_by_store"),
    path('dashboard/store:<slug:store_slug>/product:<slug:slug>/', productViewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name="single_product"),    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
