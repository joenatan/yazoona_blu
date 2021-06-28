from django.db import models


class Media(models.Model):
    woo_id = models.IntegerField()
    title = models.CharField(max_length=256)
    link = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return self.title
