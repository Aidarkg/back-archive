from rest_framework import serializers
from data_media.models import PhotoGallery


class PhotoGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoGallery
        fields = '__all__'
