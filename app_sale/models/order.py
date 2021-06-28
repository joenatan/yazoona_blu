from django.db import models


class Order(models.Model):
    woo_id = models.IntegerField(null=True)
    status = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.woo_id)


class OrderItem(models.Model):
    sku = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    price = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

    product = models.ForeignKey('woo_products.Product', on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')