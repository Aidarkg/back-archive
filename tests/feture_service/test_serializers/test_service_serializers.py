from django.test import TestCase
from apps.information.models import Service
from apps.information.serializers.service import ServiceSerializers

class ServiceSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service_data = {'title': 'Тестовая услуга', 'status': 'Активный'}
        cls.service = Service.objects.create(**cls.service_data)
        cls.serializer = ServiceSerializers(instance=cls.service)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'status']))

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.service_data['title'])

    def test_status_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['status'], self.service_data['status'])

    def test_deserialize_valid_data(self):
        valid_data = {'title': 'Новая услуга', 'status': 'Активный'}
        serializer = ServiceSerializers(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, valid_data)

    def test_deserialize_invalid_data(self):
        invalid_data = {'title': '', 'status': 'Активный'}
        serializer = ServiceSerializers(data=invalid_data)
        self.assertFalse(serializer.is_valid())
