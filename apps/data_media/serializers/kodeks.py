from rest_framework import serializers
from apps.data_media.models.kodeks import KODEKS


class KODEKSSerializer(serializers.ModelSerializer):
    class Meta:
        model = KODEKS
        fields = ('id', 'document_number', 'date_file', 'title', 'pdf_file')
