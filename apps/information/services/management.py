from ..models import Management


class ManagementService:
    @staticmethod
    def get_managements():
        return Management.objects.prefetch_related('managements_education').all()
