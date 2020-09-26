from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect


def change_language(request, language):
    response = HttpResponseRedirect('/')

    translation.activate(language)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
