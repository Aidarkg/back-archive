from rest_framework import serializers
from apps.contacts.models.anticor_cases_models import Anticore


class AnticoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anticore
        fields = ['location', 'phone_number', 'email']
