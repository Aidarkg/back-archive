from rest_framework import serializers

from apps.data_media.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'description', 'public_date')
