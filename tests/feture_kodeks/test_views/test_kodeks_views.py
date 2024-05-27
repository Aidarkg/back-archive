from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.data_media.models.kodeks import KODEKS
from apps.data_media.serializers.kodeks import KODEKSSerializer

class KODEKSSerializerTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.kodeks = KODEKS.objects.create(title='Тестовый кодекс', pdf_file='test.pdf')

    def test_kodeks_serializer(self):
        serializer_data = KODEKSSerializer(instance=self.kodeks).data
        expected_data = {
            'id': self.kodeks.id,
            'title': 'Тестовый кодекс',
            'pdf_file': 'test.pdf'

        }
        self.assertEqual(serializer_data, expected_data)

    def test_create_kodeks(self):
        data = {'title': 'Новый кодекс', 'pdf_file': 'new_test.pdf'}
        response = self.client.post(reverse('kodeks-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(KODEKS.objects.count(), 2)

    def test_update_kodeks(self):
        data = {'title': 'Измененный кодекс'}
        response = self.client.put(reverse('kodeks-detail', args=[self.kodeks.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.kodeks.refresh_from_db()
        self.assertEqual(self.kodeks.title, 'Измененный кодекс')

    def test_delete_kodeks(self):
        response = self.client.delete(reverse('kodeks-detail', args=[self.kodeks.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(KODEKS.objects.filter(id=self.kodeks.id).exists())
