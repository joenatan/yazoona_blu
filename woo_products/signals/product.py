from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from config.woo_client import client as woo_client

from woo_products.models import Product
from woo_products.serializers import ProductSerializer
# from woodoo_mapping.tasks.export_attribute_to_woo import export


@receiver(post_save, sender=Product)
def on_product_saved(sender, instance, created, **kwargs):
    # export.apply_async((instance.pk,), countdown=3)
    data = ProductSerializer(instance).data

    if not created:
        request = woo_client.put("products/%s" % instance.woo_id, data)
        print(request.json())
