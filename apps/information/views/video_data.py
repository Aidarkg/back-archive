from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from apps.information.serializers.video_data import VideoDataSerializer, VideoLinkSerializer
from apps.information.models import VideoData, VideoLink
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class VideoLinkAPIView(ListAPIView):
    queryset = VideoLink.objects.all()
    serializer_class = VideoLinkSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
