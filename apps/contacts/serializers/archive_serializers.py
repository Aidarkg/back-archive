from rest_framework import serializers
from apps.contacts.models.archive_models import ArchiveContact, Reception, Schedule, ReadingRoom


class ReadingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingRoom
        fields = ['weekdays']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['weekdays', '_break', 'weekend']


class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ['weekdays']


class GeneralSerializer(serializers.ModelSerializer):
    reception = ReceptionSerializer(many=True, read_only=True)
    schedule = ScheduleSerializer(many=True, read_only=True)
    reading_room = ReadingRoomSerializer(many=True, read_only=True)

    class Meta:
        model = ArchiveContact
        fields = ['location', 'phone_number', 'email', 'reception', 'schedule', 'reading_room']
