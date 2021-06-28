import logging
import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from woo_media.models import Media
from woo_media.serializers import MediaImportSerializer

logger = logging.getLogger(__name__)
woo_url = settings.WOO_URL


class Command(BaseCommand):
    help = "Import products from woocommerce"

    #def add_arguments(self, parser):
    #    parser.add_argument("json_file", nargs="+", type=str)

    def handle(self, *args, **options):
        logger.info('starting')
        print('starting')

        get_params = {"per_page": 100}

        request = requests.get('%s/wp-json/wp/v2/media' % woo_url, params=get_params)
        response_headers = request.headers
        print(response_headers)
        total_pages = int(response_headers.get('X-WP-TotalPages', 0))

        print("total pages: %s" % total_pages)
        page = 1
        while page < total_pages:
            params = {"page": page}
            print({**get_params, **params})
            page_request = requests.get('%s/wp-json/wp/v2/media' % woo_url, params={**get_params, **params}).json()
            print("get %s media" % len(page_request))

            for woo_media in page_request:
                obj = MediaImportSerializer(woo_media).data

                print(woo_media['id'])
                # Update is needed to disable the signals
                if Media.objects.filter(woo_id=woo_media['id']).count() > 0:
                    Media.objects.filter(woo_id=woo_media['id']).update(**obj)
                else:
                    Media(**obj).save()

            page = page + 1






