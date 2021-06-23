from rest_framework import serializers

from woo_products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    regular_price = serializers.SerializerMethodField()
    sale_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'sku', 'status', 'regular_price', 'sale_price', 'stock_quantity']

    def get_regular_price(self, obj):
        return str(obj.regular_price)

    def get_sale_price(self, obj):
        return str(obj.regular_price)


class ProductImportSerializer(serializers.ModelSerializer):
    woo_id = serializers.IntegerField(source='id')
    regular_price = serializers.SerializerMethodField(read_only=True)
    sale_price = serializers.SerializerMethodField(read_only=True)
    stock_quantity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['woo_id', 'name', 'sku', 'regular_price', 'sale_price', 'stock_quantity']

    def get_regular_price(self, obj):
        regular_price = obj['regular_price']
        if regular_price == '':
            regular_price = 0.0
        return regular_price

    def get_sale_price(self, obj):
        sale_price = obj['sale_price']
        if sale_price == '':
            sale_price = 0.0
        return sale_price

    def get_stock_quantity(self, obj):
        stock_quantity = obj['stock_quantity']
        if stock_quantity is None:
            stock_quantity = 0
        return stock_quantity