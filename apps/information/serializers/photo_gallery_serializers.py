from rest_framework import serializers
from apps.information.models import PhotoGallery, Photo


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'picture', 'count_photo', 'public_date']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']


class PhotoGallerySerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=False)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'public_date', 'picture', 'photo']
