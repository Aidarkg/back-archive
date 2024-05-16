from django.urls import path
from django.views.decorators.cache import cache_page
from apps.data_media.views import VideoDataAPIView, VideoDataRetrieveAPIView, \
    NewsListAPIView, NewsDetailAPIView, \
    PhotoGalleryListAPIView, PhotoGalleryDetailAPIView,  \
    ServiceListView, \
    KODEKSListCreateAPIView, KODEKSRetrieveUpdateDestroyAPIView, \
    SearchAPIView, ContactListAPIView, ContactDetailAPIView, \
    VisitorsAPIView, \
    ManagementListAPIView, ManagementDetailAPIView
from apps.data_media.views.organization import OrganizationListView

urlpatterns = [
    path('api/v1/video/',cache_page(60)(VideoDataAPIView.as_view()), name='video-data-list'),
    path('api/v1/video/<int:pk>',cache_page(60) (VideoDataRetrieveAPIView.as_view()), name='video-data-detail'),
    path('api/v1/management/', cache_page(60)(ManagementListAPIView.as_view()), name='management-list'),
    path('api/v1/management/<int:pk>/', cache_page(60)(ManagementDetailAPIView.as_view()), name='management-detail'),
    path('api/v1/news/', cache_page(60)(NewsListAPIView.as_view()) , name='news-list'),
    path('api/v1/news/<int:pk>/',cache_page(60)(NewsDetailAPIView.as_view()), name='news-detail'),
    path('api/v1/photos/', cache_page(60)(PhotoGalleryListAPIView.as_view()), name='photo-gallery-list'),
    path('api/v1/photos/<int:pk>/', cache_page(60)(PhotoGalleryDetailAPIView.as_view()), name='photo-gallery-detail'),
    path('api/v1/service/', cache_page(60)(ServiceListView.as_view()), name='services-list'),
    path('api/v1/kodeks/', cache_page(60)(KODEKSListCreateAPIView.as_view()), name='kodeks-list'),
    path('api/v1/kodeks/<int:pk>/', cache_page(60)(KODEKSRetrieveUpdateDestroyAPIView.as_view()), name='kodeks-detail'),
    path('api/v1/contacts', cache_page(60)(ContactListAPIView.as_view()), name='contacts-list'),
    path('api/v1/contacts/<int:pk>', cache_page(60)(ContactDetailAPIView.as_view()), name='contacts-detail'),
    path('api/v1/search/', cache_page(60)(SearchAPIView.as_view()), name='search'),
    path('api/v1/visitors/', cache_page(60)(VisitorsAPIView.as_view()), name='visitors-list'),
    path('api/v1/organizations/', cache_page(60)(OrganizationListView.as_view()), name='organizations'),

]
