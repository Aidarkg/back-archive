from django.core.files.storage import default_storage
from django.test import TestCase
from apps.data_media.models.photo_gallery_models import PhotoGallery
from apps.data_media.serializers.photo_gallery_serializers import PhotoGallerySerializer
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


def get_test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100), 'white')  # Создаём простое белое изображение
    image.save(file, 'JPEG')
    file.seek(0)
    return SimpleUploadedFile('test.jpg', file.read(), content_type='image/jpeg')


class PhotoGallerySerializerTestCase(TestCase):
    def setUp(self):
        self.photo = PhotoGallery.objects.create(
            title='Test photo',
            description='Test description',
            picture=get_test_image()
        )
        self.serializer = PhotoGallerySerializer(self.photo)

    def test_serializer_fields(self):
        expected_fields = {
            'title',
            'description',
            'picture'
        }
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    def test_serialized_fields(self):
        expected_title = 'Test photo'
        expected_description = 'Test description'
        picture_url = self.serializer.data['picture']

        self.assertEqual(self.serializer.data['title'], expected_title)
        self.assertEqual(self.serializer.data['description'], expected_description)
        self.assertTrue(picture_url.endswith('.jpg'))

    def tearDown(self):
        for photo in PhotoGallery.objects.all():
            if photo.picture:
                if default_storage.exists(photo.picture.name):
                    default_storage.delete(photo.picture.name)
            photo.delete()
