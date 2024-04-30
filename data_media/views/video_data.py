from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from data_media.serializers.video_data import VideoDataSerializer
from data_media.models import VideoData


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['title']
    

class VideoDataRetriveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    lookup_url_kwarg = 'id'
    