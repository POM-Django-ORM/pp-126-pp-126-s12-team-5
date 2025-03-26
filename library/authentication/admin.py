# Register your models here.
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'is_active', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
