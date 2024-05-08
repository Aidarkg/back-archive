from rest_framework import serializers
from ..models.management import Management


class ManagementSerializers(serializers.ModelSerializer):

    class Meta:
        model = Management
        fields = (
            'full_name',
            'image',
            'position',
            'experience'
        )
