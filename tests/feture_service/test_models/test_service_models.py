from django.test import TestCase
from apps.information.models.service import Service

class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем объект услуги для использования в тестах
        Service.objects.create(title='Тестовая услуга', status='Активный')

    def test_title_content(self):
        service = Service.objects.get(id=1)
        expected_object_name = f'{service.title}'
        self.assertEquals(expected_object_name, 'Тестовая услуга')

    def test_status_content(self):
        service = Service.objects.get(id=1)
        expected_object_status = f'{service.status}'
        self.assertEquals(expected_object_status, 'Активный')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Service._meta.verbose_name_plural), 'Услуги')

    def test_ordering(self):
        self.assertEqual(Service._meta.ordering, ['-created_at'])
