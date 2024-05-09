from rest_framework.generics import RetrieveAPIView, ListAPIView

from apps.data_media.serializers.quick_contacts_serializers import ContactSerializer
from apps.data_media.models.quick_contacts_models import Contact


class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
