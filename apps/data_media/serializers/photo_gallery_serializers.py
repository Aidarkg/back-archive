from rest_framework import serializers
from apps.data_media.models import PhotoGallery, Photo


class PhotoListSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'picture', 'count_photo', 'public_date']

    def get_picture(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.picture.url)
        return obj.picture.url


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']


class PhotoGallerySerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=False)

    class Meta:
        model = PhotoGallery
        fields = ['id', 'title', 'description', 'public_date', 'picture', 'photo']
