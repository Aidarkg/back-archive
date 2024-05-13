from django.core.files.storage import default_storage
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
from apps.data_media.models.photo_gallery_models import PhotoGallery

from datetime import date
from django.test import TestCase


class PhotoGalleryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.gallery = PhotoGallery.objects.create(
            title='Test Gallery',
            description='A description here',
            picture=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'some image content here',
                content_type='image/jpeg'
            )
        )

    # Проверяем, что метод __str__ возвращает ожидаемую строку.
    def test_string_representation(self):
        self.assertEqual(str(self.gallery), 'Test Gallery')

    # Проверяем, что ограничение по длине для поля title установлено корректно.
    def test_title_max_length(self):
        max_length = self.gallery._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    # Проверяем, что объект, который мы создали, является инстансом модели PhotoGallery.
    def test_object_creation(self):
        self.assertTrue(isinstance(self.gallery, PhotoGallery))

    # Проверяем, что путь для загрузки картинок установлен правильно.
    def test_picture_upload_to(self):
        path = self.gallery._meta.get_field('picture').upload_to
        self.assertEquals(path, 'gallery')

    # Проверяем содержимое полей, убеждаясь, что они соответствуют заданным значениям.
    def test_field_content(self):
        self.assertEqual(self.gallery.title, 'Test Gallery')
        self.assertEqual(self.gallery.description, 'A description here')

    def tearDown(self):
        # Удаление всех объектов PhotoGallery и связанных файлов изображений
        for photo in PhotoGallery.objects.all():
            if photo.picture:
                if default_storage.exists(photo.picture.name):
                    default_storage.delete(photo.picture.name)
            photo.delete()
