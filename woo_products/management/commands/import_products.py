import logging

from django.core.management.base import BaseCommand, CommandError

from config.woo_client import client as woo_client

from woo_products.models import Product
from woo_products.serializers import ProductImportSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import products from woocommerce"

    #def add_arguments(self, parser):
    #    parser.add_argument("json_file", nargs="+", type=str)

    def handle(self, *args, **options):
        logger.info('starting')
        print('starting')

        get_params = {"type": "simple"}

        request = woo_client.get("products", params=get_params)
        response_headers = request.headers

        total_pages = int(response_headers.get('X-WP-TotalPages', 0))

        print("total pages: %s" % total_pages)
        page = 1
        while page < total_pages+1:
            params = {"page": page}
            print({**get_params, **params})
            page_request = woo_client.get("products", params={**get_params, **params}).json()
            print("get %s products" % len(page_request))

            for woo_product in page_request:
                obj = ProductImportSerializer(woo_product).data

                print(obj)
                # Update is needed to disable the signals
                if Product.objects.filter(woo_id=woo_product['id']).count() > 0:
                    Product.objects.filter(woo_id=woo_product['id']).update(**obj)
                else:
                    Product(**obj).save()

            page = page + 1


