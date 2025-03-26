# Register your models here.
from django.contrib import admin
from .models import Book, Order

# Реєстрація моделі Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'count')  # Поля, що відображаються в списку
    search_fields = ('name', 'description')  # Поля для пошуку
    list_filter = ('count',)  # Поля для фільтрації

# Реєстрація моделі Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')  # Поля для списку
    search_fields = ('user__email', 'book__name')  # Пошук по користувачу та книзі
    list_filter = ('created_at', 'end_at')  # Фільтри за датами
