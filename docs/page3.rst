Surveillance avec Sentry.
=========================

- En pré-requis vous devriez avoir un acompte sur Sentry, puis avoir installé sentry-sdk avec pip:
- Le package est déjà préinstallé avec requirement.txt, donc c'est fait.
- Sentry est ensuite initialisé dans oc_lettings_site/settings.py :
Init Sentry:
------------
- Renseigner le nom de votre nouveau projet dans Sentry.
- Vous pouvez le DSN dans les références de votre projet avec [Project] > Settings > Client Keys (DSN).
- Copie cette valeur dans .env (DSN="...."). Cette valeur sera liée dans votre fichier oc_lettings_site/settings.py.
- .env non commité, `DSN` ne doit pas être diffusée avec git en production.)
- sentry_sdk.init(dsn,
                integrations=[DjangoIntegration()],
                max_breadcrumbs=50,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
                debug=False,
                )

- Nous avons la possibilité de vérifier le fonctionnement de Sentry:
# urls.py
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]
