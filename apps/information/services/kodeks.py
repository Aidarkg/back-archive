from apps.information.models import KODEKS


class KodeksService:
    @staticmethod
    def get_all_kodeks():
        return KODEKS.objects.all()
