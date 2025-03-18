
from django.contrib import admin
from django.urls import path,include
from Sellers.views import*
from Store.views import*
from Products.views import*
from dashboard.views import*
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
routers = DefaultRouter()
routers.register(r"user", SellerViewSet,basename="user")
routers.register(r"stores", storeViewset ,basename="stores")
routers.register(r"products", productViewset ,basename="products")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(routers.urls)),
    path('api/login/',LoginView.as_view(),name="login_api"),
    path('<slug:store_slug>/',productViewset.as_view({'get':'list'}),name="product_by_store"),
    path('profile/',UserProfileView.as_view(),name="profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
