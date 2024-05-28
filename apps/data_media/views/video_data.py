from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from apps.data_media.serializers.video_data import VideoDataSerializer
from apps.data_media.models import VideoData
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class VideoDataRetrieveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
