from rest_framework import serializers

from data_media.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'image', 'description', 'detailed_description', 'public_date')
