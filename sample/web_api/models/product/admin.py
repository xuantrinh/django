from django.contrib import admin
from .model import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'title','image', 'score', 'created_at', 'updated_at' ]
    list_filter = ['name', 'title', 'score']
    search_fields = ['name']
    list_per_page = 20