from rest_framework.views import APIView
from rest_framework.response import Response
from apps.information.models import Emblem
from apps.information.serializers import EmblemSerializer


class EmblemAPIView(APIView):
    def get(self, request):
        emblems = Emblem.objects.all()
        serializer = EmblemSerializer(emblems, many=True, context={'request': request})
        return Response(serializer.data)
