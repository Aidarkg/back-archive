from rest_framework import serializers
from apps.contacts.models.coll_center_models import CollCenter


class CollCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollCenter
        fields = ['number']
