from django.http import HttpResponsePermanentRedirect
from .models import RedirectRule

class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rule = RedirectRule.objects.filter(source=request.path, active=True).first()
        if rule:
            return HttpResponsePermanentRedirect(rule.target)
        return self.get_response(request)
