from rest_framework import serializers

from apps.information.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = ('id', 'title', 'logo')

    def get_logo(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.logo.url)
        return obj.logo.url
