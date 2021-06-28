import logging

from django.core.management.base import BaseCommand, CommandError

from config.woo_client import client as woo_client

from app_sale.models import Order
from app_sale.serializers import OrderImportSerializer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Import orders from woocommerce"

    #def add_arguments(self, parser):
    #    parser.add_argument("json_file", nargs="+", type=str)

    def handle(self, *args, **options):
        logger.info('starting')
        print('starting')

        get_params = {}

        request = woo_client.get("orders", params=get_params)
        response_headers = request.headers

        total_pages = int(response_headers.get('X-WP-TotalPages', 0))

        print("total pages: %s" % total_pages)
        page = 1
        while page < total_pages+1:
            params = {"page": page}
            print({**get_params, **params})
            page_request = woo_client.get("orders", params={**get_params, **params}).json()
            print("get %s products" % len(page_request))

            for woo_order in page_request:
                obj = OrderImportSerializer(woo_order).data

                print(obj)
                # Update is needed to disable the signals
                if Order.objects.filter(woo_id=woo_order['id']).count() > 0:
                    Order.objects.filter(woo_id=woo_order['id']).update(**obj)
                else:
                    Order(**obj).save()

            page = page + 1


