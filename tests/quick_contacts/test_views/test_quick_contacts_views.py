from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.information.models.quick_contacts_models import Contact


class QuickContactAPITests(APITestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            address='Test address',
            phone='0555777111',
            email='test@gmail.com',
            work_time='Test work time',
            reception='Test reception',
            reading_room='Test reading room'
        )
        self.contact2 = Contact.objects.create(
            address='Test address 2',
            phone='0555777222',
            email='test2@gmail.com',
            work_time='Test work time 2',
            reception='Test reception 2',
            reading_room='Test reading room 2'
        )
        self.list_url = reverse('contacts-list')
        self.detail_url = reverse('contacts-detail', kwargs={'pk': self.contact.pk})

    def test_contact_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)

        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_contact_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['address'], 'Test address')
        self.assertEqual(response.data['email'], 'test@gmail.com')
