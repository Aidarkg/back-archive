from rest_framework.test import APITestCase
from apps.contacts.models.archive_models import ArchiveContact, Reception, Schedule, ReadingRoom
from apps.contacts.serializers.archive_serializers import ReadingRoomSerializer, ScheduleSerializer, ReceptionSerializer, GeneralSerializer


class ReadingRoomSerializerTest(APITestCase):

    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='123 Main St, City, Country',
            phone_number='+1234567890',
            email='test@example.com'
        )
        self.reading_room_data = {'weekdays': 'Monday to Friday', 'general': self.archive_contact}
        self.reading_room = ReadingRoom.objects.create(**self.reading_room_data)
        self.serializer = ReadingRoomSerializer(instance=self.reading_room)

    def test_reading_room_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'weekdays'})

    def test_reading_room_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['weekdays'], self.reading_room_data['weekdays'])


class ScheduleSerializerTest(APITestCase):

    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='123 Main St, City, Country',
            phone_number='+1234567890',
            email='test@example.com'
        )
        self.schedule_data = {
            'weekdays': 'Monday to Friday',
            '_break': '12:00 - 13:00',
            'weekend': 'Saturday and Sunday',
            'general': self.archive_contact
        }
        self.schedule = Schedule.objects.create(**self.schedule_data)
        self.serializer = ScheduleSerializer(instance=self.schedule)

    def test_schedule_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'weekdays', '_break', 'weekend'})

    def test_schedule_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['weekdays'], self.schedule_data['weekdays'])
        self.assertEqual(data['_break'], self.schedule_data['_break'])
        self.assertEqual(data['weekend'], self.schedule_data['weekend'])


class ReceptionSerializerTest(APITestCase):

    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='123 Main St, City, Country',
            phone_number='+1234567890',
            email='test@example.com'
        )
        self.reception_data = {'weekdays': 'Monday to Friday', 'general': self.archive_contact}
        self.reception = Reception.objects.create(**self.reception_data)
        self.serializer = ReceptionSerializer(instance=self.reception)

    def test_reception_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'weekdays'})

    def test_reception_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['weekdays'], self.reception_data['weekdays'])


class GeneralSerializerTest(APITestCase):

    def setUp(self):
        self.archive_contact_data = {
            'location': '123 Main St, City, Country',
            'phone_number': '+1234567890',
            'email': 'test@example.com'
        }
        self.archive_contact = ArchiveContact.objects.create(**self.archive_contact_data)

        self.reception_data = {'weekdays': 'Monday to Friday', 'general': self.archive_contact}
        self.schedule_data = {
            'weekdays': 'Monday to Friday',
            '_break': '12:00 - 13:00',
            'weekend': 'Saturday and Sunday',
            'general': self.archive_contact
        }
        self.reading_room_data = {'weekdays': 'Monday to Friday', 'general': self.archive_contact}

        self.reception = Reception.objects.create(**self.reception_data)
        self.schedule = Schedule.objects.create(**self.schedule_data)
        self.reading_room = ReadingRoom.objects.create(**self.reading_room_data)

        self.serializer = GeneralSerializer(instance=self.archive_contact)

    def test_general_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         {'location', 'phone_number', 'email', 'reception', 'schedule', 'reading_room'})

    def test_general_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['location'], self.archive_contact_data['location'])
        self.assertEqual(data['phone_number'], self.archive_contact_data['phone_number'])
        self.assertEqual(data['email'], self.archive_contact_data['email'])
        self.assertEqual(len(data['reception']), 1)
        self.assertEqual(len(data['schedule']), 1)
        self.assertEqual(len(data['reading_room']), 1)
        self.assertEqual(data['reception'][0]['weekdays'], self.reception_data['weekdays'])
        self.assertEqual(data['schedule'][0]['weekdays'], self.schedule_data['weekdays'])
        self.assertEqual(data['schedule'][0]['_break'], self.schedule_data['_break'])
        self.assertEqual(data['schedule'][0]['weekend'], self.schedule_data['weekend'])
        self.assertEqual(data['reading_room'][0]['weekdays'], self.reading_room_data['weekdays'])
