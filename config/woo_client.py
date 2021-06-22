from woocommerce import API

from django.conf import settings


client = API(
    url=settings.WOO_URL,
    consumer_key=settings.WOO_KEY,
    consumer_secret=settings.WOO_SECRET,
    version="wc/v3",
    timeout=15
)