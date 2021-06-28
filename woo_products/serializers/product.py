from rest_framework import serializers

from woo_products.models import Product
from woo_media.models import Media


class MediaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='woo_id')

    class Meta:
        model = Media
        fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    regular_price = serializers.SerializerMethodField()
    sale_price = serializers.SerializerMethodField()
    acf = serializers.SerializerMethodField()
    images = MediaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'sku', 'status', 'description', 'regular_price', 'sale_price', 'stock_quantity', 'acf', 'images']

    def get_regular_price(self, obj):
        return str(obj.regular_price)

    def get_sale_price(self, obj):
        if obj.sale_price == 0.0:
            return ""
        return str(obj.sale_price)

    def get_acf(self, obj):
        print(obj.images.select_related())
        images = obj.images.select_related()
        # variant_image
        variant_image = ''
        if images.count() == 1:
            variant_image = images[0].woo_id
        if images.count() > 1:
            variant_image = images[1].woo_id

        # variant_title
        variant_title = obj.name.split('-')[-1]
        return {'variant_title': variant_title.strip(), "variant_image": variant_image}


class ProductImportSerializer(serializers.ModelSerializer):
    woo_id = serializers.IntegerField(source='id')
    regular_price = serializers.SerializerMethodField(read_only=True)
    sale_price = serializers.SerializerMethodField(read_only=True)
    stock_quantity = serializers.SerializerMethodField(read_only=True)
    brand = serializers.SerializerMethodField(read_only=True)
    collection = serializers.SerializerMethodField(read_only=True)
    family = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['woo_id', 'name', 'sku', 'status', 'description', 'regular_price', 'sale_price', 'stock_quantity', 'brand', 'collection', 'family']

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

    def get_brand(self, obj):
        attributes = obj.get('attributes', [])
        if len(attributes) > 0:
            t = [d for d in attributes if d['id'] == 6]
            if len(t) > 0:
                return t[0]['options'][0]
        return ''

    def get_collection(self, obj):
        attributes = obj.get('attributes', [])
        if len(attributes) > 0:
            t = [d for d in attributes if d['id'] == 5]
            if len(t) > 0:
                return t[0]['options'][0]
        return ''

    def get_family(self, obj):
        attributes = obj.get('attributes', [])
        if len(attributes) > 0:
            t = [d for d in attributes if d['id'] == 4]
            if len(t) > 0:
                return t[0]['options'][0]
        return ''
