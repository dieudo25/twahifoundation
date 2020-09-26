from django.conf import settings
from django.utils import translation
from django.http import HttpResponseRedirect


def change_language(request, language):
    response = HttpResponseRedirect('/')

    if language:
        redirect_path = f'/{language}/'

    translation.activate(language)
    response = HttpResponseRedirect(redirect_path)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
