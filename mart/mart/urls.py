
from django.contrib import admin
from django.urls import path,include
from Sellers.views import*
from Store.views import*
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
routers = DefaultRouter()
routers.register(r"sellers", SellerViewSet,basename="seller")
routers.register(r"store", storeViewset ,basename="store")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include(routers.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
