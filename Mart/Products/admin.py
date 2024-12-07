from django.contrib import admin
from .models import *
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('name','store','price','created','stock','is_available')
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Products,productAdmin)



