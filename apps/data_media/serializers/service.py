from rest_framework import serializers
from ..models.service import *


class ServiceSerializers(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'content', 'price', 'status']

    def get_head(self, obj):
        return obj.head.title
