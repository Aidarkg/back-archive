from django.test import TestCase
from apps.contacts.models import ArchiveContact, Reception, Schedule, ReadingRoom


class ArchiveContactModelTest(TestCase):
    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )

    def test_archive_contact_str(self):
        self.assertEqual(str(self.archive_contact), 'Test Location')

    def test_archive_contact_verbose_name_plural(self):
        self.assertEqual(ArchiveContact._meta.verbose_name_plural, 'Архив')


class ReceptionModelTest(TestCase):
    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )
        self.reception = Reception.objects.create(
            weekdays='Test Weekdays',
            general=self.archive_contact
        )

    def test_reception_str(self):
        self.assertEqual(str(self.reception), 'Test Weekdays')

    def test_reception_verbose_name(self):
        self.assertEqual(Reception._meta.verbose_name, 'Приём граждан')


class ScheduleModelTest(TestCase):
    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )
        self.schedule = Schedule.objects.create(
            weekdays='Test Weekdays',
            _break='Test Break',
            weekend='Test Weekend',
            general=self.archive_contact
        )

    def test_schedule_str(self):
        self.assertEqual(str(self.schedule), 'Test Weekdays')

    def test_schedule_verbose_name(self):
        self.assertEqual(Schedule._meta.verbose_name, 'График работы')


class ReadingRoomModelTest(TestCase):
    def setUp(self):
        self.archive_contact = ArchiveContact.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )
        self.reading_room = ReadingRoom.objects.create(
            weekdays='Test Weekdays',
            general=self.archive_contact
        )

    def test_reading_room_str(self):
        self.assertEqual(str(self.reading_room), 'Test Weekdays')

    def test_reading_room_verbose_name(self):
        self.assertEqual(ReadingRoom._meta.verbose_name, 'Читальный зал')
