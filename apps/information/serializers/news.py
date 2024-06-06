from rest_framework import serializers

from apps.information.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image', 'public_date')
