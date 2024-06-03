from rest_framework import serializers
from apps.information.models import Logo


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ['logo']
