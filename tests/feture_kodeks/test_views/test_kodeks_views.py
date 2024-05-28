from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.data_media.models.kodeks import KODEKS

class KodeksAPITests(APITestCase):
    def setUp(self):
        self.kodeks = KODEKS.objects.create(
            title='Test title for Kodeks',
            pdf_file='Test pdf_file for Kodeks',

        )
        self.kodeks2 = KODEKS.objects.create(
            title='Test title 2 for Kodeks',
            pdf_file='Test pdf_file 2 for Kodeks',

        )
        self.list_url = reverse('kodeks-list')
        self.detail_url = reverse('kodeks-detail', kwargs={'pk': self.kodeks.pk})

    def test_kodeks_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)

        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_kodeks_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['title'], 'Test title for Kodeks')
        self.assertEqual(response.data['pdf_file'], 'http://testserver/media/Test%20pdf_file%20for%20Kodeks')

