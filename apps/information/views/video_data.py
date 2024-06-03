from rest_framework.response import Response
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

        queryset = list(video_file) + list(video_link)

        page = paginator.paginate_queryset(queryset, request)

        serializer = []

        for obj in page:
            if isinstance(obj, VideoData):
                serializer.append({'video_file': (VideoDataSerializer(obj, context={'request': request})).data})
            elif isinstance(obj, VideoLink):
                serializer.append({'video_link': (VideoLinkSerializer(obj, context={'request': request})).data})

        return paginator.get_paginated_response(serializer)
