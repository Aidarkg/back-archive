from rest_framework import serializers
from apps.data_media.models.kodeks import KODEKS


class KODEKSSerializer(serializers.ModelSerializer):
    class Meta:
        model = KODEKS
        fields = ('title', 'pdf_file')
