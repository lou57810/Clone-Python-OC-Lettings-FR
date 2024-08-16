import sentry_sdk
from sentry_sdk import capture_message
from django.shortcuts import render


def index(request):
    return render(request, 'lettings/home.html')


def custom404(request, *args, **kwargs):
    capture_message("Page not found!", level="error")
    return render(request, 'error404.html')


def custom500(request, *args, **kwargs):
    capture_message("Error 500!", level="error")
    return render(request, 'error500.html', status=500)


def trigger_error(request):
    """
    Déclenche une erreur de division par zéro pour tester
    la capture d'exception par Sentry.

    Args:
        request (HttpRequest): L'objet HttpRequest
        qui représente la requête HTTP.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente
        la réponse HTTP contenant la page d'erreur.

    """
    try:
        return 1 / 0
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
