from rest_framework.test import APITestCase
from apps.contacts.models.anticor_cases_models import Anticore
from apps.contacts.serializers.anticor_cases_serializers import AnticoreSerializer


class AnticoreSerializerTest(APITestCase):

    def setUp(self):
        self.anticore_data = {
            'location': '123 Главная ул., Город, Страна',
            'phone_number': '+1234567890',
            'email': 'test@example.com'
        }
        self.anticore = Anticore.objects.create(**self.anticore_data)
        self.serializer = AnticoreSerializer(instance=self.anticore)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'location', 'phone_number', 'email'})

    def test_location_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['location'], self.anticore_data['location'])

    def test_phone_number_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['phone_number'], self.anticore_data['phone_number'])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.anticore_data['email'])

    def test_create_valid_data(self):
        serializer = AnticoreSerializer(data=self.anticore_data)
        self.assertTrue(serializer.is_valid())
        anticore_instance = serializer.save()
        self.assertEqual(anticore_instance.location, self.anticore_data['location'])
        self.assertEqual(anticore_instance.phone_number, self.anticore_data['phone_number'])
        self.assertEqual(anticore_instance.email, self.anticore_data['email'])
