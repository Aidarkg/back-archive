from rest_framework import serializers
from apps.contacts.models.coll_center_models import CollCenter
from apps.contacts.serializers.archive_serializers import GeneralSerializer as ArchiveSerializer
from apps.contacts.serializers.anticor_cases_serializers import AnticoreSerializer as AnticorCasesSerializer


class CollCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollCenter
        fields = ['number']


# class GeneralSerializer(serializers.Serializer):
#     archive = ArchiveSerializer(many=True, read_only=True)
#     anticor_cases = AnticorCasesSerializer(many=True, read_only=True)
#     coll_center = CollCenterSerializer(many=True, read_only=True)

