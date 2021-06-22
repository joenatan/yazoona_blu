import logging

from django.core.management.base import BaseCommand, CommandError

from config.woo_client import client as woo_client

from woo_products.models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import products from woocommerce"

    #def add_arguments(self, parser):
    #    parser.add_argument("json_file", nargs="+", type=str)

    def handle(self, *args, **options):
        logger.info('starting')
        print('starting')

        request = woo_client.get("products")
        response_headers = request.headers

        total_pages = int(response_headers.get('X-WP-TotalPages', 0))

        print("total pages: %s" % total_pages)
        page = 1
        while page < total_pages+1:
            # add first products
            page_request = woo_client.get("products", params={"page": page}).json()
            print("get %s products" % len(page_request))

            for woo_product in page_request:
                product, created = Product.objects.get_or_create(id=woo_product['id'])

                regular_price = woo_product.get('regular_price')
                if regular_price == '':
                    regular_price = 0.0

                sale_price = woo_product.get('sale_price')
                if sale_price == '':
                    sale_price = 0.0

                stock_quantity = woo_product.get('stock_quantity')
                if stock_quantity is None:
                    stock_quantity = 0

                print(stock_quantity)
                product.name = woo_product['name']
                product.sku = woo_product['sku']
                product.status = woo_product['status']
                product.regular_price = regular_price
                product.sale_price = sale_price
                product.stock_quantity = stock_quantity

                product.save()

            page = page + 1


