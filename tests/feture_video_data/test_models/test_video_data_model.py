from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.information.models.video_data import VideoData, VideoLink
from datetime import datetime

class VideoDataTestCase(TestCase):
    def setUp(self):
        self.video_data = VideoData.objects.create(
            video='path/to/video.mp4',
            title='Test Video',
            public_date=datetime.now()
        )

    def test_video_data_creation(self):
        self.assertEqual(self.video_data.title, 'Test Video')
        self.assertEqual(self.video_data.__str__(), 'Test Video')

    def test_verbose_name_plural(self):
        self.assertEqual(str(VideoData._meta.verbose_name_plural), 'Видеогалерея')

class VideoLinkTestCase(TestCase):
    def setUp(self):
        self.video_link = VideoLink.objects.create(
            title='Test Video Link',
            video_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            public_date=datetime.now()
        )

    def test_video_link_creation(self):
        self.assertEqual(self.video_link.title, 'Test Video Link')
        self.assertEqual(self.video_link.__str__(), 'Test Video Link')

    def test_verbose_name_plural(self):
        self.assertEqual(str(VideoLink._meta.verbose_name_plural), 'Видео ссылка')

    def test_invalid_video_link(self):
        with self.assertRaises(ValidationError):
            invalid_video_link = VideoLink.objects.create(
                title='Invalid Video Link',
                video_link='invalid_link',
                public_date=datetime.now()
            )
            invalid_video_link.full_clean()
