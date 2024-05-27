from datetime import date
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.data_media.models import Visitors
from apps.data_media.serializers import VisitorSerializer


class VisitorsAPIView(APIView):
    def get(self, request):
        visitor, created = Visitors.objects.get_or_create(pk=1)
        visitor.increase_count()
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)
