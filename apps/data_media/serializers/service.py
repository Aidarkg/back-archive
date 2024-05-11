from rest_framework import serializers
from apps.data_media.models import Service


class ServiceSerializers(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Service
        fields = ('id', 'content', 'price', 'status')
