from django.contrib import admin
from .models import User
# Register your models here.
class sellerAdmin(admin.ModelAdmin):
    list_display = ('email','phone_number','is_buyer','is_seller','is_staff','is_active',)
    list_filter = ('is_buyer','is_seller','is_staff','is_active',)
    search_fields = ('email',)
    readonly_fields = ("password",)
admin.site.register(User,sellerAdmin)