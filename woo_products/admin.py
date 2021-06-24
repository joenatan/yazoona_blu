from django.contrib import admin

from .models import Product, ProductContact


class ProductContactInline(admin.TabularInline):
    model = ProductContact
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'sku']
    list_display = ['sku', 'name', 'stock_quantity', 'suppliers']
    list_filter = ['status']
    inlines = [ProductContactInline]

    def suppliers(self, obj):
        suppliers = obj.suppliers.select_related().values('purchase_sku', 'contact__name')
        return list(['%s (%s)' %(d['purchase_sku'], d['contact__name']) for d in suppliers])