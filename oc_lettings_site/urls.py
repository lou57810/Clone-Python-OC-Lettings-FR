from django.contrib import admin
from django.urls import path, include
from . import views
from oc_lettings_site.views import home  # index


""" Liste de modèles urls. A chaque requête HTTP, Django parcourt cette liste dans l'ordre
    et essaie de trouver une correspondance. """


urlpatterns = [
    path('', home, name='home'),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('error/', views.custom500, name='oc_lettings_error'),
    path('error', views.custom500, name='oc_lettings_error'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', views.trigger_error, name='sentry_test'),
    ]
