from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView

from data_media.serializers.quick_contacts_serializers import ContactSerializer
from data_media.models.quick_contacts_models import Contact


# get - Возвращает список объектов
class ContactListAPIView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# get_object - возвращает объект класса по id
# get - Получение одной вариации
class ContactDetailAPIView(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'


