from rest_framework.generics import ListAPIView

from apps.contacts.models import Contact
from apps.contacts.serializers.contact_serializers import ContactSerializer


class ContactListAPIView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
