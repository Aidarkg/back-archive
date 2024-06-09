import os
from datetime import datetime, date
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from apps.information.models import KODEKS
from apps.information.serializers.kodeks import KODEKSSerializer


class KODEKSSerializerTest(TestCase):
    def setUp(self):
        self.kodeks_data = {
            'title': 'Example Title',
            'pdf_file': 'path/to/valid_pdf_file.pdf',
            'date_file': date.today(),
            'document_number': 5
        }
        self.kodeks = KODEKS.objects.create(**self.kodeks_data)
        self.serializer = KODEKSSerializer(instance=self.kodeks)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            {'id', 'title', 'pdf_file', 'date_file', 'document_number'}
        )

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.kodeks_data['title'])

    def test_pdf_file_field_content(self):
        data = self.serializer.data
        self.assertEqual(os.path.basename(data['pdf_file']), os.path.basename(self.kodeks_data['pdf_file']))

    def test_validation_with_valid_data(self):
        # Создаем временный файл
        test_file = SimpleUploadedFile("test_file.pdf", b"file_content", content_type="application/pdf")

        # Подготавливаем данные для сериализации
        data = {
            'title': 'Test title',
            'pdf_file': test_file,
            'date_file': date.today(),
            'document_number': 5
        }

        # Создаем сериализатор и проверяем валидацию
        serializer = KODEKSSerializer(data=data)
        self.assertTrue(serializer.is_valid(), msg=serializer.errors)

    def test_validation_with_invalid_data(self):
        invalid_data = {'title': '', 'pdf_file': ''}
        serializer = KODEKSSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
