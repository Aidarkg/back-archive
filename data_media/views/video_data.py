from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from data_media.serializers.video_data import VideoDataSerializer
from data_media.models import VideoData


class VideoDataAPIView(ListAPIView):
    queryset = VideoData.objects.all().order_by('-created_at')
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = VideoData.objects.all()

        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )
        
        return queryset
    

class VideoDataRetriveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    lookup_url_kwarg = 'id'
    