from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from apps.information.models.organization import Organization
from apps.information.serializers.organization import OrganizationSerializer
from PIL import Image
from io import BytesIO


class OrganizationSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем изображение в памяти
        image = Image.new('RGB', (100, 100))
        # BytesIO используется для хранения данных в памяти
        image_file = BytesIO()
        image.save(image_file, 'png')
        image_file.seek(0)  # Возвращаем указатель на начало файла

        # Создаем объект организации с изображением
        cls.organization = Organization.objects.create(
            title='Test Organization',
            logo=SimpleUploadedFile("test_logo.png", image_file.read(), content_type="image/png")
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
        self.assertEqual(updated_organization.title, 'Updated Organization')

    def test_invalid_organization_data(self):
        invalid_data = {'title': '', 'logo': None}
        serializer = OrganizationSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
