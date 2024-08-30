from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_message, capture_exception, set_tag


def lettings_index(request):

    """ Retourne la page d'index."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    try:
        letting = Letting.objects.get(id=letting_id)
        set_tag("action", "consultation.letting")
        capture_message(f"L'utilisateur {request.user} a consulté {letting.title}")

    except Exception as e:
        set_tag("letting", f"L'utilisateur {request.user} a voulu consulter un id: {letting_id} inexistant!")
        capture_exception(e)
        return render(request, 'error404.html', {'error_message': str(e)}, status=404)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
