from apps.information.models import Service


class ServiceModelService:
    @staticmethod
    def get_all_services():
        return Service.objects.all()
