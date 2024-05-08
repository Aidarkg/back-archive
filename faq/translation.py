from modeltranslation.translator import register, TranslationOptions

from .models.faq import Faq


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
