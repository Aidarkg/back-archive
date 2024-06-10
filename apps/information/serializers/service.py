from rest_framework import serializers
from apps.information.models import Service, PriceList


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'status')


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ('file',)
