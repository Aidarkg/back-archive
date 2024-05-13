from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.data_media.models.organization import Organization
from apps.data_media.serializers.organization import OrganizationSerializer

class OrganizationAPIView(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
