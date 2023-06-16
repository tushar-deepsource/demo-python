from django.views.generic.base import View
from django.utils.html import format_html as fhtml
import django.utils.html as foo


class SomeView(View):
    @staticmethod
    def get(request):
        user = get_user()
        return fhtml(f"<em>{user.name}</em>")

    @staticmethod
    def put(request):
        user = get_user()
        return foo.format_html(f"<em>{user.name}</em>")


class FixedView(View):
    @staticmethod
    def get(request):
        user = get_user()
        return format_html("<em>{}</em>", user.name)
