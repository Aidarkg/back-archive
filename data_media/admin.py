from django.contrib import admin
# from data_media.models.news import News
# from data_media.models.photo_gallery_models import PhotoGallery
from data_media.models.video_data import VideoData


@admin.register(VideoData)
class VideoDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_display_links = ('id', 'title')

    fields = ('id', 'video', 'title', 'description', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

# admin.site.register(PhotoGallery)
# admin.site.register(News)