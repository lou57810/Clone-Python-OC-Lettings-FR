from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_message, capture_exception, set_tag


def lettings_index(request):

    """ Retourne la page d'index."""
    current_url = request.build_absolute_uri()
    # print('current_url:', current_url)
    # Vérifier si l'URL est alphanumérique et correspond à l'URL attendue

    """ Retourne une liste de locations. 
    if current_url.isalnum() or current_url == 'http://127.0.0.1:8000/lettings/index/':
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    else:
        return render(request, 'error404.html')"""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    try:
        letting = Letting.objects.get(id=letting_id)
    except Exception as e:
        capture_message("Page not found Error 404!", level="error")
        set_tag("letting", f"L'utilisateur {request.user} a voulu consulter un id: {letting_id} inexistant!")
        capture_exception(e)
        return render(request, 'error404.html', {'error_message': str(e)}, status=404)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    capture_message(f"L'utilisateur, {request.user} a consulte lettings {letting.title}")
    return render(request, 'lettings/letting.html', context)
