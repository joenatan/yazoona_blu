from django import forms
from django_select2 import forms as s2forms

from config.form_components import BaseAutocompleteSelect
from woo_products.models import Product
from woo_media.models import Media


class MediaAutocompleteWidget(BaseAutocompleteSelect):
    empty_label = "-- select book --"
    search_fields = ("title__icontains",)
    queryset = Media.objects.order_by("title")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "images": MediaAutocompleteWidget
        }