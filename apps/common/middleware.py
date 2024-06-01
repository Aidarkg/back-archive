import re
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def base_url(self, request):
        url = request.build_absolute_uri()
        pattern = r'^https?://[^/]+'
        match = re.match(pattern, url)
        base_url = match.group()
        return base_url

    def process_exception(self, request, exception):
        if isinstance(exception, PermissionDenied):
            return render(
                request,
                'errors/403.html',
                status=403,
                context={'url': self.base_url(request)}
            )
        elif isinstance(exception, Http404):
            return render(
                request,
                'errors/404.html',
                status=404,
                context={'url': self.base_url(request)}
            )

        return None

