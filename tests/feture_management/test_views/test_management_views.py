from django.test import TestCase
from rest_framework.test import APIRequestFactory
from apps.information.views.management import ManagementListAPIView, ManagementDetailAPIView
from apps.information.models.management import Management


class ManagementListAPIViewTest(TestCase):
    def setUp(self):
        # Создаем несколько объектов Management
        self.management1 = Management.objects.create(full_name='Test Name 1', position='Test Position 1',
                                                     start_year=2020)
        self.management2 = Management.objects.create(full_name='Test Name 2', position='Test Position 2',
                                                     start_year=2021)

    def test_get_managements_list(self):
        # Создаем запрос к API
        factory = APIRequestFactory()
        request = factory.get('/managements/')

        # Получаем ответ от представления
        view = ManagementListAPIView.as_view()
        response = view(request)

        # Проверяем, что запрос завершился успешно
        self.assertEqual(response.status_code, 200)

        # Получаем список данных из ответа
        data_list = response.data['results']

        # Проверяем, что представление вернуло правильное количество объектов
        self.assertEqual(len(data_list), 2)

        # Проверяем, что представление вернуло правильные данные для каждого объекта
        self.assertTrue(any(item['id'] == self.management1.id for item in data_list))
        self.assertTrue(any(item['id'] == self.management2.id for item in data_list))


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
