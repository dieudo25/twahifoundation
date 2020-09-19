from django.shortcuts import render


def custom_page_not_found_view(request, exception):
    return render(request, "page/errors/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "page/errors/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "page/errors/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "page/errors/400.html", {})
