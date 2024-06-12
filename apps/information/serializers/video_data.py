from rest_framework import serializers
from apps.information.models.video_data import VideoData, VideoLink


class VideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoData
        fields = ('title', 'video', 'public_date')


class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLink
        fields = ('title', 'video_link', 'public_date')
