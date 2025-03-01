from django.contrib import admin
from .models import User
# Register your models here.
class sellerAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
admin.site.register(User,sellerAdmin)