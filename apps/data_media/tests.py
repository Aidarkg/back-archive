from rest_framework.test import APITestCase
from rest_framework import status
from apps.data_media.models.organization import Organization
import json
class OrganizationGetAPITest(APITestCase):

    def setUp(self):
        self.organization_data = {
            'title': 'Test Organization',
            'logo': 'Test organization logo',

        }
        self.organization = Organization.objects.create(**self.organization_data)

    def test_get_organization_list(self):

        response = self.client.get('http://127.0.0.1:8000/api/v1/organizations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn(self.organization.title, [org['title'] for org in response.data])
