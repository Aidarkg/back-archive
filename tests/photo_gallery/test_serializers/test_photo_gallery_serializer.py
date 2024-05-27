from django.core.files.storage import default_storage
from django.test import TestCase
from apps.data_media.models.photo_gallery_models import PhotoGallery, Photo
from apps.data_media.serializers.photo_gallery_serializers import PhotoGallerySerializer, PhotoSerializer
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


class PhotoGallerySerializerTestCase(TestCase):
    def setUp(self):
        self.picture = PhotoGallery.objects.create(
            title='Test picture',
            description='Test description',
            picture=get_test_image()
        )
        self.serializer = PhotoGallerySerializer(self.picture)

    def test_serializer_fields(self):
        expected_fields = {
            'id',
            'title',
            'description',
            'picture',
            'photo'
        }
        self.assertEqual(set(self.serializer.data.keys()), expected_fields)

    def test_serialized_fields(self):
        expected_title = 'Test picture'
        expected_description = 'Test description'
        picture_url = self.serializer.data['picture']

        self.assertEqual(self.serializer.data['title'], expected_title)
        self.assertEqual(self.serializer.data['description'], expected_description)
        self.assertTrue(picture_url.endswith('.jpg'))

    def tearDown(self):
        for picture in PhotoGallery.objects.all():
            if picture.picture:
                if default_storage.exists(picture.picture.name):
                    default_storage.delete(picture.picture.name)
            picture.delete()


class PhotoSerializerTestCase(TestCase):
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
        self.serializer = PhotoSerializer(self.photo)

    def test_photo_serializer(self):
        self.assertTrue(isinstance(self.serializer, PhotoSerializer))
        path = self.serializer.data['photo']
        self.assertEquals(path, '/media/gallery_photo/test.jpg')

    def tearDown(self):
        for photo_object in Photo.objects.all():
            if photo_object.photo:
                if default_storage.exists(photo_object.photo.name):
                    default_storage.delete(photo_object.photo.name)
            photo_object.delete()

        for photo_gallery in PhotoGallery.objects.all():
            if photo_gallery.picture:
                if default_storage.exists(photo_gallery.picture.name):
                    default_storage.delete(photo_gallery.picture.name)
            photo_gallery.delete()
