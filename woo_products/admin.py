from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    search_fields = ['name', 'sku']
    list_display = ['sku', 'name', 'stock_quantity']
    list_filter = ['status']
