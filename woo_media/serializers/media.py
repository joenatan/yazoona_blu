from rest_framework import serializers

from woo_media.models import Media


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ['title']


class MediaImportSerializer(serializers.ModelSerializer):
    woo_id = serializers.IntegerField(source='id')
    title = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['woo_id', 'title', 'link']

    def get_title(self, obj):
        return obj['title']['rendered']