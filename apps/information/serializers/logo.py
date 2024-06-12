from rest_framework import serializers
from apps.information.models import Logo, Emblem


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['logo']


class EmblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emblem
        fields = ['emblem']
