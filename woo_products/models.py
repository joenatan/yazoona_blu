from django.db import models

PRODUCT_STATUS_TYPES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
)


class Product(models.Model):
    woo_id = models.IntegerField()
    name = models.CharField(max_length=256)
    sku = models.CharField(max_length=256, blank=True)
    ean = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, default='draft', choices=PRODUCT_STATUS_TYPES)

    description = models.TextField(blank=True)

    regular_price = models.FloatField(default=0.0)
    sale_price = models.FloatField(default=0.0)

    stock_quantity = models.IntegerField(default=0)

    images = models.ManyToManyField('woo_media.Media', related_name='products')

    brand = models.CharField(max_length=256)
    collection = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    @property
    def supplier_sku(self):
        supplier = self.suppliers.select_related().first()
        if supplier:
            return supplier.purchase_sku
        return ''


class ProductContact(models.Model):
    contact = models.ForeignKey('app_contact.Contact', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='suppliers')

    purchase_sku = models.CharField(max_length=256)
    price = models.FloatField(default=0.0)
