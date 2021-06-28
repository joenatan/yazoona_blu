from rest_framework import serializers

from app_sale.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['status', 'total']


class OrderImportSerializer(serializers.ModelSerializer):
    woo_id = serializers.IntegerField(source='id')

    class Meta:
        model = Order
        fields = ['woo_id', 'status', 'total']
