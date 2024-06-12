from modeltranslation.admin import TabbedTranslationAdmin


class BaseAdminMixin(TabbedTranslationAdmin):
    search_fields = 'title',
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('title',)
    ordering = ['-created_at', '-updated_at']

    readonly_fields = ('created_at', 'updated_at')
    group_fieldsets = True
