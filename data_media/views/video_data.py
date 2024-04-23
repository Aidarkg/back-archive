from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from data_media.serializers.video_data import VideoDataSerializer
from data_media.models import VideoData
from rest_framework.response import Response
from rest_framework import status


class VideoDataAPIView(APIView):
    def get(self, request):
        video_data = VideoData.objects.all()
        serializer = VideoDataSerializer(video_data, many=True).data
        return Response(serializer)
    def post(self, request):
        serializer = VideoDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VideoDataRetriveAPIView(RetrieveAPIView):
    queryset = VideoData.objects.all()
    serializer_class = VideoDataSerializer
    lookup_url_kwarg = 'id'
    
    