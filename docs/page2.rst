Lancement de l'application en local.
====================================

- Vous devez tout d'abord activer l'environnement créé précédemment.
- En utilisant Git bash avec la commande:
  ``source venv/Scripts/activate``
- Vous pouvez confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel avec la
  commande:
  `which python`
  L'invite de commande sera précédée de `env` en cas de succès.

- Ou avec Windows PowerShell avec la commande:
  ``.\venv\Scripts\Activate.ps1``

- Une fois ceci réalisé vous devez installer les dépendances:
  ``pip install -r requirements.txt`` installe tous les packages requis pour votre application.

- L'application est prête à être démarrée:
  ``python manage.py runserver``

- Elle est disponible en local à l'adresse: ``http://127.0.0.1:8000``

- Vous avez également accès à l'administration:
- Url: ``http://127.0.0.1:8000/admin``
- Id: ``admin``
- Password: ``Abc1234!``








