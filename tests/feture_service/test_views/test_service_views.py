from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.information.models.service import Service
from apps.information.serializers import ServiceSerializers


class ServiceListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service1 = Service.objects.create(title='Тестовая услуга 1', status='Активный')
        cls.service2 = Service.objects.create(title='Тестовая услуга 2', status='Неактивный')

    def test_get_service_list(self):
        url = reverse('services-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.data['results']

        expected_data = ServiceSerializers(Service.objects.all(), many=True).data

        self.assertEqual(data, expected_data)
