from django.db import models

PRODUCT_STATUS_TYPES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
)


class Product(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=256)
    sku = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, default='draft', choices=PRODUCT_STATUS_TYPES)

    regular_price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0)

    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name