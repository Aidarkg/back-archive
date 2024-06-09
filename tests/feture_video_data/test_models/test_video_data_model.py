from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.information.models.video_data import VideoData, VideoLink


class VideoDataTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.current_time = timezone.now()
        cls.video_data = VideoData.objects.create(
            video='path/to/video.mp4',
            title='Test Video',
            public_date=cls.current_time
        )

    def test_video_data_creation(self):
        self.assertEqual(self.video_data.title, 'Test Video')
        self.assertEqual(str(self.video_data), 'Test Video')

    def test_verbose_name_plural(self):
        self.assertEqual(str(VideoData._meta.verbose_name_plural), 'Видеогалерея')


class VideoLinkTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.current_time = timezone.now()
        cls.video_link = VideoLink.objects.create(
            title='Test Video Link',
            video_link='https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            public_date=cls.current_time
        )

    def test_video_link_creation(self):
        self.assertEqual(self.video_link.title, 'Test Video Link')
        self.assertEqual(str(self.video_link), 'Test Video Link')

    def test_verbose_name_plural(self):
        self.assertEqual(str(VideoLink._meta.verbose_name_plural), 'Видео ссылка')

    def test_invalid_video_link(self):
        with self.assertRaises(ValidationError):
            invalid_video_link = VideoLink(
                title='Invalid Video Link',
                video_link='invalid_link',
                public_date=self.current_time
            )
            invalid_video_link.full_clean()
