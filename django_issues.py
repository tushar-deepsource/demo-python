"""Doc"""
import datetime

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])  # Sensitive
def current_datetime(request):
    """Doc"""
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now
    return HttpResponse(html)


def foo():
    return a or b or c or d or e or f or g or g or i or j or k
