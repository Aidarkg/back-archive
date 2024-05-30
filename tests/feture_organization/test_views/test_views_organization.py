from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.data_media.models.organization import Organization

class OrganizationListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_organizations = 10
        for organization_num in range(number_of_organizations):
            Organization.objects.create(
                title=f'Organization {organization_num}',
                logo=f'Logo {organization_num}'
            )

    def test_list_organizations(self):
        url = reverse('organizations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


