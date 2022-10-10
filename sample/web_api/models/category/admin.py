
from django.contrib import admin
from .model import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at', ]
    list_filter = ['name', ]
    search_fields = ['name']
    list_per_page = 20