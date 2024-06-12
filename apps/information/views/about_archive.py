from rest_framework.generics import ListAPIView
from apps.information.serializers import AboutArchiveSerializer
from apps.information.models import AboutArchive


class AboutArchiveAPIView(ListAPIView):
    queryset = AboutArchive.objects.all()
    serializer_class = AboutArchiveSerializer
    pagination_class = None
