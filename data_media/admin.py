from django.contrib import admin
from data_media.models import News, PhotoGallery, VideoData, Management, Service, KODEKS


class VideoDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'video', 'title', 'description', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'picture', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'title', 'description', 'picture', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'detailed_description', 'image', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'title', 'description', 'detailed_description', 'image', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

class ManagementAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'image', 'position', 'experience', 'created_at', 'updated_at']
    list_display_links = ['id', 'full_name']
    search_fields = ['full_name']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'full_name', 'image', 'position', 'experience', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

class KODEKSAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(News, NewsAdmin)
admin.site.register(VideoData, VideoDataAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Service)
admin.site.register(KODEKS, KODEKSAdmin)
