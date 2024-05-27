from django.urls import path
from apps.contacts.views.general_views import GeneralListAPIView


urlpatterns = [
    path('api/v1/contacts', GeneralListAPIView.as_view(), name='contacts-list'),
]