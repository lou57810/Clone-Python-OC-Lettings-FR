# urls.py
from django.contrib import admin
from django.urls import path, include
# from django.http import HttpResponse
# from . import views
from oc_lettings_site.views import index


# def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', index, name='home'),
    # path('sentry-debug/', trigger_error),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    ]
