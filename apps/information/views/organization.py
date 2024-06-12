from rest_framework.generics import ListAPIView
from apps.information.models.organization import Organization
from apps.information.serializers.organization import OrganizationSerializer


class OrganizationListView(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = None
