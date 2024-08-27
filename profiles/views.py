from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_message, capture_exception, set_tag


def profiles_index(request):
    try:
        """ Retourne la page d'index."""
        profiles_list = Profile.objects.all()
    except Exception as e:
        capture_message("Page not found Error 404!", level="error")
        capture_exception(e)
        return render(request, 'error404.html')

    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
        set_tag("action", "consultation.profile")
        capture_message(f"L'utilisateur {request.user} a consulté {profile.user.username}")
    except Exception as e:
        capture_exception(e)
        return render(request, 'error404.html')

    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
