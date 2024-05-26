from django.test import TestCase
from apps.data_media.models.kodeks import KODEKS

class KODEKSTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.kodeks = KODEKS.objects.create(title='Тестовый кодекс', pdf_file='test.pdf')

    def test_title(self):
        kodeks = KODEKS.objects.get(title='Тестовый кодекс')
        self.assertEqual(kodeks.title, 'Тестовый кодекс')

    def test_verbose_name(self):
        self.assertEqual(KODEKS._meta.verbose_name, 'Кодекс')

    def test_verbose_name_plural(self):
        self.assertEqual(KODEKS._meta.verbose_name_plural, 'Кодексы')

    def test_pdf_file_upload_to(self):
        upload_to = KODEKS._meta.get_field('pdf_file').upload_to
        file_path = upload_to(self.kodeks, 'test.pdf')
        self.assertEqual(file_path, 'pdf_files/test.pdf')