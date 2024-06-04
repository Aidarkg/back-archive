from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from apps.information.models import VideoData, VideoLink
from apps.information.serializers.video_data import VideoDataSerializer, VideoLinkSerializer
from apps.information.views import VideoDataAPIView, VideoLinkAPIView


class VideoDataAPIViewTest(APITestCase):
    def setUp(self):
        self.video_data = VideoData.objects.create(
            title="Test Video",
            video="test_video.mp4",
            public_date="2024-06-04"
        )
        self.factory = APIRequestFactory()

    def test_get_video_data(self):
        url = reverse('video-link-data-list')
        request = self.factory.get(url)
        response = VideoDataAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Test Video")


class VideoLinkAPIViewTest(APITestCase):
    def setUp(self):
        self.video_link = VideoLink.objects.create(
            title="Test Video Link",
            video_link="https://www.example.com/video",
            public_date="2024-06-04"
        )
        self.factory = APIRequestFactory()

    def test_get_video_link(self):
        url = reverse('video-link-data-list')
        request = self.factory.get(url)
        response = VideoLinkAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Test Video Link")
