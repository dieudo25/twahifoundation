"""twahifoundation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


import notifications.urls

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    re_path(r'^account/', include('account.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^contact/', include('contact.urls')),
    re_path(r'^message/', include('message.urls')),
    re_path(r'^newsletter/', include('newsletter.urls')),
    re_path(r'^inbox/notifications/',
            include(notifications.urls, namespace='notifications')),
    re_path(r'^paypal/', include('paypal.standard.ipn.urls')),
    re_path(r'^portal/', include('portal.urls')),
    re_path(r'^project/', include('project.urls')),
    re_path(r'^stock/', include('stock.urls')),
    re_path(r'^transaction/', include('transaction.urls')),
    re_path(r'^', include('page.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT, })
    ] + urlpatterns

handler404 = 'page.views.error.custom_page_not_found_view'
handler500 = 'page.views.error.custom_error_view'
handler403 = 'page.views.error.custom_permission_denied_view'
handler400 = 'page.views.error.custom_bad_request_view'
