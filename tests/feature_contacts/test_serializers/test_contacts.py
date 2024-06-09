from rest_framework.test import APITestCase
from apps.contacts.models import Contact
from apps.contacts.serializers.contact_serializers import ContactSerializer


class ContactSerializerTest(APITestCase):

    def setUp(self):
        self.contact_data = {
            'address': '123 Main St, City, Country',
            'phone_number': '+1234567890',
            'index': '123456',
            'fax': '+1234567891',
            'email': 'test@example.com',
            'facebook': 'https://www.facebook.com/test'
        }
        self.contact = Contact.objects.create(**self.contact_data)
        self.serializer = ContactSerializer(instance=self.contact)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'address', 'phone_number', 'index', 'fax', 'email', 'facebook'})

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['address'], self.contact_data['address'])
        self.assertEqual(data['phone_number'], self.contact_data['phone_number'])
        self.assertEqual(data['index'], self.contact_data['index'])
        self.assertEqual(data['fax'], self.contact_data['fax'])
        self.assertEqual(data['email'], self.contact_data['email'])
        self.assertEqual(data['facebook'], self.contact_data['facebook'])

    def test_create_valid_data(self):
        serializer = ContactSerializer(data=self.contact_data)
        self.assertTrue(serializer.is_valid())
        contact_instance = serializer.save()
        self.assertEqual(contact_instance.address, self.contact_data['address'])
        self.assertEqual(contact_instance.phone_number, self.contact_data['phone_number'])
        self.assertEqual(contact_instance.index, self.contact_data['index'])
        self.assertEqual(contact_instance.fax, self.contact_data['fax'])
        self.assertEqual(contact_instance.email, self.contact_data['email'])
        self.assertEqual(contact_instance.facebook, self.contact_data['facebook'])

    def test_invalid_email(self):
        invalid_data = self.contact_data.copy()
        invalid_data['email'] = 'invalid_email'
        serializer = ContactSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_blank_phone_number(self):
        invalid_data = self.contact_data.copy()
        invalid_data['phone_number'] = ''
        serializer = ContactSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('phone_number', serializer.errors)
