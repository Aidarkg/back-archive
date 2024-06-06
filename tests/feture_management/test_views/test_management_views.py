from django.test import TestCase
from rest_framework.test import APIRequestFactory
from apps.information.views.management import ManagementListAPIView, ManagementDetailAPIView
from apps.information.models.management import Management

class ManagementListAPIViewTest(TestCase):
    def setUp(self):
        # Создаем несколько объектов Management
        self.management1 = Management.objects.create(full_name='Test Name 1', position='Test Position 1', start_year=2020)
        self.management2 = Management.objects.create(full_name='Test Name 2', position='Test Position 2', start_year=2021)

    def test_get_managements_list(self):
        # Создаем запрос к API
        factory = APIRequestFactory()
        request = factory.get('/managements/')

        # Получаем ответ от представления
        view = ManagementListAPIView.as_view()
        response = view(request)

        # Проверяем, что запрос завершился успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что представление вернуло правильное количество объектов
        self.assertEqual(len(response.data['results']), 2)

        # Проверяем, что представление вернуло правильные данные для каждого объекта
        self.assertEqual(response.data['results'][0]['id'], self.management2.id)
        self.assertEqual(response.data['results'][0]['full_name'], self.management2.full_name)
        self.assertEqual(response.data['results'][0]['position'], self.management2.position)

        self.assertEqual(response.data['results'][1]['id'], self.management1.id)
        self.assertEqual(response.data['results'][1]['full_name'], self.management1.full_name)
        self.assertEqual(response.data['results'][1]['position'], self.management1.position)

class ManagementDetailAPIViewTest(TestCase):
    def test_get_management_detail(self):
        # Создаем объект Management
        management = Management.objects.create(full_name='Test Name', position='Test Position', start_year=2022)

        # Создаем запрос к API
        factory = APIRequestFactory()
        request = factory.get(f'/managements/{management.id}/')

        # Получаем ответ от представления
        view = ManagementDetailAPIView.as_view()
        response = view(request, pk=management.id)

        # Проверяем, что запрос завершился успешно
        self.assertEqual(response.status_code, 200)

        # Проверяем, что представление вернуло правильные данные для объекта
        self.assertEqual(response.data['id'], management.id)
        self.assertEqual(response.data['full_name'], management.full_name)
        self.assertEqual(response.data['position'], management.position)
