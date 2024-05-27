from rest_framework import serializers
from apps.data_media.models import Visitors


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = ['counter']
