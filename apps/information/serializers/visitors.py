from rest_framework import serializers
from apps.information.models import Visitors


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = ['counter']
