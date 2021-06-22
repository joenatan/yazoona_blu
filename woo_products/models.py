from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    sku = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, default='draft')

    regular_price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0)

    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name