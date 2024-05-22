from rest_framework import serializers
from apps.data_media.models import PhotoGallery, Photo


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'picture']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = 'photo'.split()


class PhotoGallerySerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=False)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'picture', 'photo']
