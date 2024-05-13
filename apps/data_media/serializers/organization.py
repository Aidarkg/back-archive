from rest_framework import serializers

from apps.data_media.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('title', 'logo')
