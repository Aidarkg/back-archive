from django.forms import EmailField
from apps.data_media.models.quick_contacts_models import Contact

from django.test import TestCase


class QuickContactsModelsTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            address='Test address',
            phone='0555777111',
            email='test@gmail.com',
            work_time='Test work time',
            reception='Test reception',
            reading_room='Test reading room'
        )

    def test_contact_creation(self):
        self.assertTrue(isinstance(self.contact, Contact))

    def test_field_content(self):
        self.assertEqual(self.contact.address, 'Test address')
        self.assertEqual(self.contact.email, 'test@gmail.com')

    def test_max_length(self):
        max_length_address = self.contact._meta.get_field('address').max_length
        max_length_phone = self.contact._meta.get_field('phone').max_length
        max_length_work_time = self.contact._meta.get_field('work_time').max_length
        max_length_reception = self.contact._meta.get_field('reception').max_length
        max_length_reading_room = self.contact._meta.get_field('reading_room').max_length
        self.assertEqual(max_length_address, 255)
        self.assertEqual(max_length_phone, 20)
        self.assertEqual(max_length_work_time, 100),
        self.assertEqual(max_length_reception, 100)
        self.assertEqual(max_length_reading_room, 100)
