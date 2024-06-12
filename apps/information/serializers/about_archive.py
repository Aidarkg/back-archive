from rest_framework import serializers
from apps.information.models import AboutArchive


class AboutArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutArchive
        fields = ['title', 'description', 'photo']
