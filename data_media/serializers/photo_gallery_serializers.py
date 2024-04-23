from rest_framework import serializers
from data_media.models import PhotoGallery


class PhotoGallerySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(read_only=True, view_name="data_media:photo-detail")

    class Meta:
        model = PhotoGallery
        fields = ['id', 'url', 'title', 'description', 'picture', 'created_at', 'updated_at']
