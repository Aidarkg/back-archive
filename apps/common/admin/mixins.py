from modeltranslation.admin import TranslationAdmin


class BaseAdminMixin(TranslationAdmin):
    search_fields = 'title',
    list_filter = ('created_at', 'updated_at')
    list_display_links = ('title',)
    ordering = ['created_at', 'updated_at']

    readonly_fields = ('created_at', 'updated_at')
    group_fieldsets = True

    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }
