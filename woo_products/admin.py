from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

from .forms import ProductForm
from .models import Product, ProductContact


class ProductResource(resources.ModelResource):
    supplier_sku = Field()

    class Meta:
        model = Product
        fields = ['name', 'supplier_sku', 'stock_quantity']

    def dehydrate_supplier_sku(self, obj):
        return obj.supplier_sku


class BookAdmin(ImportExportModelAdmin):
    resource_class = ProductResource


class ProductContactInline(admin.TabularInline):
    model = ProductContact
    extra = 0


@admin.register(Product)
class ProductAdmin(BookAdmin):
    search_fields = ['name', 'sku']
    list_display = ['sku', 'name', 'stock_quantity', 'suppliers']
    list_filter = ['status', 'collection']
    inlines = [ProductContactInline]
    form = ProductForm

    def suppliers(self, obj):
        suppliers = obj.suppliers.select_related().values('purchase_sku', 'contact__name')
        return list(['%s (%s)' %(d['purchase_sku'], d['contact__name']) for d in suppliers])