from rest_framework import serializers
from ..models.management import Management, ManagementEducation, ManagementWork


class ManagementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = (
            'id',
            'full_name',
            'image',
            'position',
            'start_year',
            'end_year'
        )


class ManagementEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManagementEducation
        fields = ('year', 'place', 'specialization')


class ManagementWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementWork
        fields = ('year', 'place', 'position')


class ManagementDetailsSerializers(serializers.ModelSerializer):
    managements_education = ManagementEducationSerializers(read_only=True, many=True)
    managements_work = ManagementWorkSerializer(read_only=True, many=True)

    class Meta:
        model = Management
        fields = (
            'id',
            'full_name',
            'image',
            'position',
            'birth_date',
            'clas_chin',
            'managements_education',
            'managements_work'
        )
