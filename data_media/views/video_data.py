from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from data_media.serializers.video_data import VideoDataSerializer
from data_media.models import VideoData


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all().order_by('-created_at')
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination


class VideoDataRetriveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    lookup_url_kwarg = 'id'
