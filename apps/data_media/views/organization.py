from rest_framework.generics import ListAPIView
from apps.data_media.models.organization import Organization
from apps.data_media.serializers.organization import OrganizationSerializer


class OrganizationListView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
