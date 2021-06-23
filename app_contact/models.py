from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Address(models.Model):
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256, blank=True)
    postcode = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=2)

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='addresses')

