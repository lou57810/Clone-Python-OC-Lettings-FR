import sentry_sdk
from sentry_sdk import capture_message
from django.shortcuts import render


def index(request):
    """index function for home page.

        request : HttpRequest object.
            The request sent by the client.

        response: HttpResponse object
        render home page.
    """
    return render(request, 'lettings/home.html')


def custom404(request, *args, **kwargs):
    capture_message("Page not found!", level="error")
    return render(request, 'error404.html', status=404)


def custom500(request, *args, **kwargs):
    capture_message("Error 500!", level="error")
    return render(request, 'error500.html', status=500)


def trigger_error(request):
    """
    Crée une "ZeroDivisionError" pour tester
    le rapport Sentry.
    """
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
