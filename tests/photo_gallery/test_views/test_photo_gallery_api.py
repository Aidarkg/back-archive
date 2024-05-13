from django.core.files.storage import default_storage
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.data_media.models import PhotoGallery


class PhotoGalleryAPITests(APITestCase):
    def setUp(self):
        # Добавление тестовых данных
        self.photo1 = PhotoGallery.objects.create(
            title='Photo 1',
            description='Description 1',
            picture=SimpleUploadedFile(name='test1.jpg', content=b'test1 image content', content_type='image/jpeg')
        )
        self.photo2 = PhotoGallery.objects.create(
            title='Photo 2',
            description='Description 2',
            picture=SimpleUploadedFile(name='test2.jpg', content=b'test2 image content', content_type='image/jpeg')
        )
        self.list_url = reverse('photo-gallery-list')
        self.detail_url = reverse('photo-gallery-detail', kwargs={'pk': self.photo1.pk})

    def tearDown(self):
        # Удаление всех объектов PhotoGallery и связанных файлов изображений
        for photo in PhotoGallery.objects.all():
            if photo.picture:
                if default_storage.exists(photo.picture.name):
                    default_storage.delete(photo.picture.name)
            photo.delete()

    def test_photo_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что в ответе содержатся данные о всех фотографиях
        self.assertEqual(len(response.data['results']), 2)
        # Проверяем, что пагинация работает правильно
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_photo_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что данные соответствуют запрашиваемой фотографии
        self.assertEqual(response.data['title'], 'Photo 1')
        self.assertEqual(response.data['description'], 'Description 1')
        # print(response.data)
        # self.assertTrue('test1.jpg' in response.data['picture'])
