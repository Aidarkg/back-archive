from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from apps.data_media.serializers.video_data import VideoDataSerializer
from apps.data_media.models import VideoData


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all().order_by('-created_at')
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination


class VideoDataRetrieveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
