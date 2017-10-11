from django.http import HttpResponse
from django.views import View


class HomeView(View):
    http_method_names = ['get']

    def dispatch(self, request, *args, **kwargs):
        return HttpResponse('OK')
