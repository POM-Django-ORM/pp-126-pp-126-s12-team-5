# Register your models here.
from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'biography')
    search_fields = ('first_name', 'last_name')
