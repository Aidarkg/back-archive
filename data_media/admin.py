from django.contrib import admin
from common.admin.mixins import BaseAdminMixin
from data_media.models import News, PhotoGallery, VideoData, Management, Service, KODEKS


class VideoDataAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']
    fields = ['id', 'video', 'title', 'description', 'created_at', 'updated_at']


class PhotoGalleryAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'description', 'picture', 'created_at', 'updated_at']
    fields = ['id', 'title', 'description', 'picture', 'created_at', 'updated_at']


class NewsAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'description', 'detailed_description', 'image', 'created_at', 'updated_at']
    fields = ['id', 'title', 'description', 'detailed_description', 'image', 'created_at', 'updated_at']


class ManagementAdmin(BaseAdminMixin):
    list_display = ['id', 'full_name', 'image', 'position', 'experience', 'created_at', 'updated_at']
    list_display_links = ['id', 'full_name']
    search_fields = ['full_name']

    fields = ['id', 'full_name', 'image', 'position', 'experience', 'created_at', 'updated_at']


class KODEKSAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']
    fields = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']


admin.site.register(News, NewsAdmin)
admin.site.register(VideoData, VideoDataAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Service)
admin.site.register(KODEKS, KODEKSAdmin)
