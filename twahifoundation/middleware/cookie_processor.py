""" class DjangoLanguageCookieProcessingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if not request.COOKIES.get('cookie_consent_level'):
            response.delete_cookie('django_language')

        return response """