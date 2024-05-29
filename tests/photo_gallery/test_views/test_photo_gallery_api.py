from django.core.files.storage import default_storage
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO
from apps.information.models import PhotoGallery


def get_test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100), 'white')  # Создаём простое белое изображение
    image.save(file, 'JPEG')
    file.seek(0)
    return SimpleUploadedFile('test.jpg', file.read(), content_type='image/jpeg')


class PhotoGalleryAPITests(APITestCase):
    def setUp(self):
        self.photo1 = PhotoGallery.objects.create(
            title='Photo 1',
            description='Description 1',
            picture=get_test_image()
        )
        self.photo2 = PhotoGallery.objects.create(
            title='Photo 2',
            description='Description 2',
            picture=get_test_image()
        )
        self.list_url = reverse('photo-gallery-list')
        self.detail_url = reverse('photo-gallery-detail', kwargs={'pk': self.photo1.pk})

    def tearDown(self):
        for photo in PhotoGallery.objects.all():
            if photo.picture:
                if default_storage.exists(photo.picture.name):
                    default_storage.delete(photo.picture.name)
            photo.delete()

    def test_photo_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)

        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_photo_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['title'], 'Photo 1')
        self.assertEqual(response.data['description'], 'Description 1')
