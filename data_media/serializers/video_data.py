from rest_framework import serializers
from data_media.models.video_data import VideoData


class VideoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoData
        fields = ('title', 'description', 'video')
