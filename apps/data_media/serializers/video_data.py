from rest_framework import serializers
from apps.data_media.models.video_data import VideoData


class VideoDataSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = VideoData
        fields = ('id', 'title', 'description', 'video', 'public_date')

    def get_video(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.video.url)
        return obj.video.url
