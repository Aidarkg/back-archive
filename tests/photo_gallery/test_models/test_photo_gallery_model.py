from django.core.files.storage import default_storage
from apps.information.models.photo_gallery_models import PhotoGallery, Photo

from django.test import TestCase

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


def get_test_image():
    file = BytesIO()
    image = Image.new('RGB', (100, 100), 'white')  # Создаём простое белое изображение
    image.save(file, 'JPEG')
    file.seek(0)
    return SimpleUploadedFile('test.jpg', file.read(), content_type='image/jpeg')


def delete_files_and_objects(objects, file_field):
    for obj in objects:
        file = getattr(obj, file_field)
        if file:
            if default_storage.exists(file.name):
                default_storage.delete(file.name)
        obj.delete()


class PhotoGalleryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.gallery = PhotoGallery.objects.create(
            title='Test Gallery',
            description='A description here',
            picture=get_test_image()
        )

    def test_string_representation(self):
        self.assertEqual(str(self.gallery), 'Test Gallery')

    # def test_title_max_length(self):
    #     max_length = self.gallery._meta.get_field('title').max_length
    #     self.assertEquals(max_length, 50)

    def test_object_creation(self):
        self.assertTrue(isinstance(self.gallery, PhotoGallery))

    def test_picture_upload_to(self):
        path = self.gallery._meta.get_field('picture').upload_to
        self.assertEquals(path, 'gallery/logo')

    def test_field_content(self):
        self.assertEqual(self.gallery.title, 'Test Gallery')
        self.assertEqual(self.gallery.description, 'A description here')

    def tearDown(self):
        delete_files_and_objects(PhotoGallery.objects.all(), 'picture')


class PhotoTestCase(TestCase):
    def setUp(self):
        self.gallery = PhotoGallery.objects.create(
            title='Test Gallery',
            description='A description here',
            picture=get_test_image()
        )
        self.photo = Photo.objects.create(
            gallery=self.gallery,
            photo=get_test_image()
        )

    def test_photo_creation(self):
        self.assertTrue(isinstance(self.photo, Photo))
        path = self.photo._meta.get_field('photo').upload_to
        self.assertEquals(path, 'gallery_photo')

    def test_photo_gallery_relation(self):
        self.assertEqual(self.photo.gallery, self.gallery)

    def test_display_image(self):
        photo_image = Image.open(self.photo.photo.path)
        self.assertIsNotNone(photo_image)

    def tearDown(self):
        delete_files_and_objects(Photo.objects.all(), 'photo')
        delete_files_and_objects(PhotoGallery.objects.all(), 'picture')
