from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory
from apps.information.models import VideoData, VideoLink
from apps.information.serializers import VideoDataSerializer, VideoLinkSerializer

class VideoDataSerializerTest(TestCase):
    def setUp(self):
        self.video_data = VideoData.objects.create(
            title="Test Video",
            video=SimpleUploadedFile("test_video.mp4", b"file_content"),
            public_date="2024-06-04"
        )
        self.factory = APIRequestFactory()

    def test_video_field(self):
        serializer = VideoDataSerializer(instance=self.video_data)
        request = self.factory.get('/')
        serializer.context['request'] = request
        data = serializer.data
        self.assertIn('video', data)
        self.assertEqual(data['video'], request.build_absolute_uri(self.video_data.video.url))


class VideoLinkSerializerTest(TestCase):
    def setUp(self):
        self.video_link = VideoLink.objects.create(
            title="Test Video Link",
            video_link="https://www.example.com/video",
            cover=SimpleUploadedFile("test_cover.jpg", b"image_content"),
            public_date="2024-06-04"
        )

    def test_serialization(self):
        serializer = VideoLinkSerializer(instance=self.video_link)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'title', 'video_link', 'cover', 'public_date'})
        self.assertEqual(data['title'], "Test Video Link")
        self.assertEqual(data['video_link'], "https://www.example.com/video")
        self.assertEqual(data['cover'], self.video_link.cover.url)
        self.assertEqual(data['public_date'], "2024-06-04")
