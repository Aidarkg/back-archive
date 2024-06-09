from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from django.utils import timezone
from apps.information.models import VideoData
from apps.information.views import VideoDataAPIView
from django.core.files.uploadedfile import SimpleUploadedFile


class VideoDataAPIViewTest(APITestCase):
    def setUp(self):
        # Создаем тестовый видеофайл
        video_content = b"file_content"
        self.video_data = VideoData.objects.create(
            title="Test Video",
            video=SimpleUploadedFile("test_video.mp4", video_content),
            public_date=timezone.now().date()
        )
        self.factory = APIRequestFactory()

    def test_get_video_data(self):
        url = reverse('video-data-list')
        request = self.factory.get(url)
        response = VideoDataAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Test Video")
