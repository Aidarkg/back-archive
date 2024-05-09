from rest_framework import serializers
from data_media.models.quick_contacts_models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'address', 'email', 'work_time', 'reception', 'reading_room']
