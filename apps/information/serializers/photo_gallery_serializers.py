from rest_framework import serializers
from apps.information.models import PhotoGallery, Photo, PhotoHome


class PhotoListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'picture', 'public_date', 'count']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']


class PhotoGallerySerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=False)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'public_date', 'picture', 'photo']


class PhotoHomeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoHome
        fields = ['id', 'photo']


class PhotoHomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoHome
        fields = ['photo', 'title', 'description']
