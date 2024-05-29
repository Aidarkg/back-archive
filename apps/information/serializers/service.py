from rest_framework import serializers
from apps.information.models import Service


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'status')
