from django.test import TestCase
from apps.data_media.models.quick_contacts_models import Contact
from apps.data_media.serializers.quick_contacts_serializers import ContactSerializer


class PhotoGallerySerializerTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            address='Test address',
            phone='0555777111',
            email='test@gmail.com',
            work_time='Test work time',
            reception='Test reception',
            reading_room='Test reading room'
        )

        self.serializer = ContactSerializer(self.contact)

    def test_serializer_fields(self):
        expected_fields = {
            'address',
            'phone',
            'email',
            'work_time',
            'reception',
            'reading_room',
        }
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    def test_serialized_fields(self):
        expected_address = 'Test address'
        expected_phone = '0555777111'
        expected_email = 'test@gmail.com'
        expected_work_time = 'Test work time'
        expected_reception = 'Test reception'
        expected_reading_room = 'Test reading room'

        self.assertEqual(self.serializer.data['address'], expected_address)
        self.assertEqual(self.serializer.data['phone'], expected_phone)
        self.assertEqual(self.serializer.data['email'], expected_email)
        self.assertEqual(self.serializer.data['work_time'], expected_work_time)
        self.assertEqual(self.serializer.data['reception'], expected_reception)
        self.assertEqual(self.serializer.data['reading_room'], expected_reading_room)
