from django.contrib import admin

from app_sale.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['woo_id', 'total']
    inlines = [OrderItemInline]