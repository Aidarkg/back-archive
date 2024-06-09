from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from apps.contacts.models import archive_models, anticor_cases_models, coll_center_models
from apps.contacts.serializers import archive_serializers, anticor_cases_serializers, general_serializers


class GeneralListAPIViewTest(APITestCase):
    url = reverse('contacts-list')  # Предполагается, что у вас есть имя маршрута для этого представления

    def setUp(self):
        # Создаем тестовые данные
        archive = archive_models.ArchiveContact.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )
        anticor_case = anticor_cases_models.Anticore.objects.create(
            location='Test Location',
            phone_number='123456789',
            email='test@example.com'
        )
        coll_center = coll_center_models.CollCenter.objects.create(
            number='123456789',
        )

    def test_general_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем наличие ключей в возвращаемых данных
        self.assertIn('archive', response.data)
        self.assertIn('anticor', response.data)
        self.assertIn('coll_center', response.data)

        # Проверяем, что данные сериализованы корректно
        self.assertEqual(len(response.data['archive']), 1)
        self.assertEqual(len(response.data['anticor']), 1)
        self.assertEqual(len(response.data['coll_center']), 1)

        # Проверяем, что данные совпадают с ожидаемыми данными
        archive_data = response.data['archive'][0]
        self.assertEqual(archive_data['location'], 'Test Location')
        self.assertEqual(archive_data['phone_number'], '123456789')
        self.assertEqual(archive_data['email'], 'test@example.com')

        anticor_data = response.data['anticor'][0]
        self.assertEqual(archive_data['location'], 'Test Location')
        self.assertEqual(anticor_data['phone_number'], '123456789')
        self.assertEqual(anticor_data['email'], 'test@example.com')

        coll_center_data = response.data['coll_center'][0]
        self.assertEqual(coll_center_data['number'], '123456789')
