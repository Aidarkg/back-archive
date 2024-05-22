from rest_framework.views import APIView
from rest_framework.response import Response
from apps.data_media.models import News, KODEKS, PhotoGallery, VideoData, Service, Management
from apps.data_media.serializers import NewsSerializer,  PhotoSerializer, VideoDataSerializer, ServiceSerializers
from django.db.models import Q

from apps.data_media.serializers.kodeks import KODEKSSerializer
from apps.data_media.serializers.management import ManagementSerializers


class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('search', None)
        if query is not None:
            news = News.objects.filter(Q(title__icontains=query))
            codexes = KODEKS.objects.filter(title__icontains=query)
            photos = PhotoGallery.objects.filter(title__icontains=query)
            videos = VideoData.objects.filter(title__icontains=query)
            services = Service.objects.filter(title__icontains=query)
            managementes = Management.objects.filter(full_name__icontains=query)

            results = {
                'news': NewsSerializer(news, many=True).data,
                'codexes': KODEKSSerializer(codexes, many=True).data,
                'photos': PhotoSerializer(photos, many=True).data,
                'videos': VideoDataSerializer(videos, many=True).data,
                'services': ServiceSerializers(services, many=True).data,
                'managementes': ManagementSerializers(managementes, many=True).data

            }

            return Response(results)
        return Response({"message": "Поисковый запрос не предоставлен"}, status=400)
