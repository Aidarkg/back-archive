from datetime import datetime, timedelta
from django.utils import timezone
from django.test import TestCase
from apps.information.models.news import News


class NewsModelTestCase(TestCase):
    def setUp(self):
        # Сохраняем текущее время
        self.current_time = timezone.now()
        # Создаем новость с текущим временем
        self.news = News.objects.create(
            title='Test News Title',
            description='Test news description. Lorem ipsum dolor sit amet.',
            public_date=self.current_time
        )

    def test_news_creation(self):
        self.assertTrue(isinstance(self.news, News))

    def test_field_description(self):
        self.assertEqual(self.news.title, 'Test News Title')
        self.assertEqual(self.news.description, 'Test news description. Lorem ipsum dolor sit amet.')
        # Сравниваем время с погрешностью в 1 секунду
        self.assertAlmostEqual(self.news.public_date, self.current_time, delta=timedelta(seconds=1))

    def test_max_length(self):
        max_length_title = self.news._meta.get_field('title').max_length
        max_length_description = self.news._meta.get_field('description').max_length
        self.assertEqual(max_length_title, 500)
        self.assertEqual(max_length_description, None)

    def test_publication_date_format(self):
        # Проверяем, что поле public_date содержит объект типа datetime
        self.assertIsInstance(self.news.public_date, datetime)
        # Проверяем, что время в поле public_date равно текущему времени
        self.assertEqual(self.news.public_date, self.current_time)

    def test_verbose_name_plural(self):
        self.assertEqual(str(News._meta.verbose_name_plural), 'Публикации')
