from django.contrib import admin
from data_media.models import News, PhotoGallery, VideoData, Management, Service


@admin.register(VideoData)
class VideoDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('id', 'title')

    fields = ('id', 'video', 'title', 'description', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

admin.site.register(Management)
admin.site.register(PhotoGallery)
admin.site.register(News)
admin.site.register(Service)