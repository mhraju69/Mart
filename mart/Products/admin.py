from django.contrib import admin
from .models import Products
# Register your models here.
class productAdmin(admin.ModelAdmin):
    prepopulated_fields={'product_slug':('name',)}
admin.site.register(Products,productAdmin)
