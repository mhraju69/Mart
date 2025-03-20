from django.contrib import admin
from .models import Store
# Register your models here.
class storeAdmin(admin.ModelAdmin):
    prepopulated_fields={'store_slug':('name',)}
admin.site.register(Store,storeAdmin)