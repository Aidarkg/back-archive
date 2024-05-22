from django.test import TestCase
from apps.data_media.models.news import News
from apps.data_media.serializers.news import NewsSerializer


class NewsSerializerTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            title='Test News Title',
            description='Test news description. Lorem ipsum dolor sit amet.',
            public_date='2024-05-20'
        )

        self.serializer = NewsSerializer(self.news)

    def test_serializer_fields(self):
        expected_fields = {
            'title',
            'description',
            'public_date'
        }
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    def test_serialized_fields(self):
        expected_title = 'Test News Title'
        expected_description = 'Test news description. Lorem ipsum dolor sit amet.'
        expected_public_date = '2024-05-20'

        self.assertEqual(self.serializer.data['title'], expected_title)
        self.assertEqual(self.serializer.data['description'], expected_description)
        self.assertEqual(self.serializer.data['public_date'], expected_public_date)

    def test_empty_fields(self):
        news_without_title = News.objects.create(
            description='Test news description without title.',
            public_date='2024-05-21'
        )
        serializer = NewsSerializer(news_without_title)
        self.assertNotIn('title', serializer.data)

    def test_invalid_data_format(self):
        with self.assertRaises(ValueError):
            News.objects.create(
                title='Invalid Date Format',
                description='Test news description with invalid date format.',
                public_date='2024/05/20'
            )


        serializer = NewsSerializer(News.objects.all(), many=True)
        self.assertEqual(len(serializer.data), 2)
