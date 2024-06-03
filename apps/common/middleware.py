from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.db import IntegrityError
from apps.common.utils import set_current_request


def base_url(request):
    scheme = request.scheme
    host = request.get_host()
    url = f'{scheme}://{host}'
    return url


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_current_request(request)
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(request, exception):
        if isinstance(exception, PermissionDenied):
            return render(
                request,
                'errors/403.html',
                status=403,
                context={'url': base_url(request)}
            )
        elif isinstance(exception, Http404):
            return render(
                request,
                'errors/404.html',
                status=404,
                context={'url': base_url(request)}
            )
        elif isinstance(exception, IntegrityError):
            return render(
                request,
                'errors/unique.html',
                status=500,
                context={'url': base_url(request)}
            )

        return None
