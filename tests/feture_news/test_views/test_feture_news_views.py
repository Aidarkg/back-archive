from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.data_media.models.news import News


class NewsAPITests(APITestCase):
    def setUp(self):
        self.news = News.objects.create(
            title='Test title',
            description='Test content',
            publish_date='2024-05-20',
        )
        self.news2 = News.objects.create(
            title='Test title 2',
            description='Test content 2',
            publish_date='2024-05-21',
        )
        self.list_url = reverse('news-list')
        self.detail_url = reverse('news-detail', kwargs={'pk': self.news.pk})

    def test_news_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)

        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_news_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['title'], 'Test title')
        self.assertEqual(response.data['description'], 'Test description')
