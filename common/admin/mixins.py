from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


class BaseAdminMixin(TranslationAdmin):
    search_fields = 'title',
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('id', 'title')

    readonly_fields = ('id', 'created_at', 'updated_at')
