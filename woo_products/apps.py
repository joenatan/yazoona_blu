from django.apps import AppConfig


class WooProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'woo_products'

    def ready(self):
        import woo_products.signals
