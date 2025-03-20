
from django.contrib import admin
from django.urls import path,include
from User.views import*
from Store.views import*
from Products.views import*
from dashboard.views import*
from cart.views import*
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
routers = DefaultRouter()
routers.register(r"cart", CartViewset,basename="cart")
routers.register(r"user", UserViewSet,basename="user")
routers.register(r"stores", storeViewset ,basename="stores")
routers.register(r"products", productViewset ,basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(routers.urls)),
    path('api/login/',LoginView.as_view(),name="login_api"),
    path('dashboard/',DashboardAPI.as_view({'get':'user'}),name='profile'),
    path('dashboard/store/',storeViewset.as_view({'get':'get_store','post':'create'}),name='store_by_user'),
    path('dashboard/store:<slug:store_slug>/',storeViewset.as_view({'get':'get_store','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name="product_by_store"),
    path('dashboard/store:<slug:store_slug>/product/', productViewset.as_view({'get': 'get_product', 'post':'create'}),name="product_by_store"),    
    path('dashboard/store:<slug:store_slug>/product:<slug:product_slug>/', productViewset.as_view({'get': 'get_product', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name="single_product"),    
    path('cart/',CartViewset.as_view({'get': 'get_cartitems'}),name='cartview'),
    path('cart:<slug:product_slug>/',CartViewset.as_view({'get': 'get_cartitems','post':'create','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name='cartview'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
