from django.test import TestCase
from apps.information.models.news import News
from apps.information.serializers.news import NewsSerializer



class NewsSerializerTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(
            title='Test News Title',
            image='Test News Image',
            description='Test news description. Lorem ipsum dolor sit amet.',
            detailed_description='Test news detailed. Lorem ipsum dolor sit amet.',
            public_date='2024-05-20',
        )

        self.serializer = NewsSerializer(self.news)

    def test_serializer_fields(self):
        expected_fields = {
            'title',
            'image',
            'description',
            'detailed_description',
            'public_date',
        }
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    def test_serialized_fields(self):
        expected_title = 'Test News Title'
        expected_image = '/media/Test%20News%20Image'
        expected_description = 'Test news description. Lorem ipsum dolor sit amet.'
        expected_detailed_description = 'Test news detailed. Lorem ipsum dolor sit amet.'
        expected_public_date = '2024-05-20'

        self.assertEqual(self.serializer.data['title'], expected_title)
        self.assertEqual(self.serializer.data['image'], expected_image)
        self.assertEqual(self.serializer.data['description'], expected_description)
        self.assertEqual(self.serializer.data['detailed_description'], expected_detailed_description)
        self.assertEqual(self.serializer.data['public_date'], expected_public_date)



