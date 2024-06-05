from rest_framework import serializers

from apps.information.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'title', 'logo')
