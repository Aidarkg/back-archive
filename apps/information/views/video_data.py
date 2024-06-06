from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from apps.information.serializers.video_data import VideoDataSerializer, VideoLinkSerializer
from apps.information.models import VideoData, VideoLink
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class VideoDataAPIView(APIView):

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        paginator = PageNumberPagination()

        video_file = VideoData.objects.all()
        video_link = VideoLink.objects.all()

        ser_video_file = VideoDataSerializer(video_file, many=True, context={'request': request}).data
        ser_video_link = VideoLinkSerializer(video_link, many=True, context={'request': request}).data

        combined_data = ser_video_file + ser_video_link

        paginate_data = paginator.paginate_queryset(combined_data, request)

        return paginator.get_paginated_response(paginate_data)
