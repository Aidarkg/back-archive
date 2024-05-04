from django.contrib import admin


class BaseAdminMixin(admin.ModelAdmin):
    search_fields = 'title',
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('id', 'title')

    readonly_fields = ('id', 'created_at', 'updated_at')
