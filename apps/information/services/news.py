from apps.information.models import News


class NewsService:
    @staticmethod
    def get_all_news():
        return News.objects.all()
