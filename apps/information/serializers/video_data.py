from rest_framework import serializers
from apps.information.models.video_data import VideoData, VideoLink


class VideoDataSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = VideoData
        fields = ('title', 'video', 'public_date')

    def get_video(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.video.url)
        return obj.video.url


class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLink
        fields = ('title', 'video_link', 'cover', 'public_date')
