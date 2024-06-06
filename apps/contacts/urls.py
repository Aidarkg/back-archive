from django.urls import path
from apps.contacts.views.general_views import GeneralListAPIView


urlpatterns = [
    path('contacts/', GeneralListAPIView.as_view(), name='contacts-list'),
]
