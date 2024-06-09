import os
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from apps.information.models.kodeks import KODEKS


class KODEKSTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pdf_file = SimpleUploadedFile('test.pdf', b'test_content')
        date_file = datetime.now()
        document_number = 2
        cls.kodeks = KODEKS.objects.create(
            title='Тестовый кодекс',
            pdf_file=pdf_file,
            date_file=date_file,
            document_number=document_number
        )

    def test_title(self):
        kodeks = KODEKS.objects.get(title='Тестовый кодекс')
        self.assertEqual(kodeks.title, 'Тестовый кодекс')

    def test_verbose_name(self):
        self.assertEqual(KODEKS._meta.verbose_name, 'НПА')

    def test_verbose_name_plural(self):
        self.assertEqual(KODEKS._meta.verbose_name_plural, 'НПА')

    def test_upload_to(self):
        expected_dir = 'pdf_files'
        actual_path = self.kodeks.pdf_file.name

        self.assertTrue(actual_path.startswith(expected_dir))

        self.assertTrue(os.path.basename(actual_path).startswith('test'))
