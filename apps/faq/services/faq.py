from apps.faq.models import Faq


class FaqService:
    @staticmethod
    def get_faqs():
        return Faq.objects.all()
