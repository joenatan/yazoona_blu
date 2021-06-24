from django.db import models


class ProductContact(models.Model):
    contact = models.ForeignKey('app_contact.Contact', on_delete=models.CASCADE)
    product = models.ForeignKey('woo_products.Product', on_delete=models.CASCADE)

    purchase_sku = models.CharField(max_length=256)
