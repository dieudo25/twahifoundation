from django.conf import settings
from django.http import HttpResponseRedirect


def change_language(request, language):
    response = HttpResponseRedirect('/')

    if language == 'fr':
        redirect_path = f'/{language}/'
    else:
        redirect_path = '/'
    from django.utils import translation
    translation.activate(language)
    response = HttpResponseRedirect(redirect_path)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
