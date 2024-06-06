from django.test import TestCase
from apps.information.models.news import News


class NewsModelTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            title='Test News Title',
            description='Test news description. Lorem ipsum dolor sit amet.',
            public_date='2024-05-20'
        )

    def test_news_creation(self):
        self.assertTrue(isinstance(self.news, News))

    def test_field_description(self):
        self.assertEqual(self.news.title, 'Test News Title')
        self.assertEqual(self.news.description, 'Test news description. Lorem ipsum dolor sit amet.')
        self.assertEqual(self.news.public_date, '2024-05-20')

    def test_max_length(self):
        max_length_title = self.news._meta.get_field('title').max_length
        max_length_description = self.news._meta.get_field('description').max_length
        self.assertEqual(max_length_title, 255)
        self.assertEqual(max_length_description, None)

    def test_publication_date_format(self):
        self.assertIsInstance(self.news.public_date, str)

    def test_verbose_name_plural(self):
        self.assertEqual(str(News._meta.verbose_name_plural), 'Новости')
