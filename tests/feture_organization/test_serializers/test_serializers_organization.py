from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from apps.data_media.models.organization import Organization
from apps.data_media.serializers.organization import OrganizationSerializer

class OrganizationSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.organization = Organization.objects.create(
            title='Test Organization',
            logo=SimpleUploadedFile("test_logo.png", b"file_content", content_type="image/png")
        )

    def test_organization_serializer(self):
        serializer = OrganizationSerializer(instance=self.organization)
        data = serializer.data

        self.assertEqual(data['title'], 'Test Organization')
        self.assertTrue('logo' in data)
        self.assertIsNotNone(data['logo'])

    def test_update_organization(self):
        data = {'title': 'Updated Organization'}
        serializer = OrganizationSerializer(instance=self.organization, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_organization = serializer.save()
        self.assertEqual(updated_organization.title,
                         'Updated Organization')

    def test_invalid_organization_data(self):
        invalid_data = {'title': '', 'logo': None}
        serializer = OrganizationSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())


