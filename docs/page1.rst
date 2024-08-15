Bienvenue sur la documentation du site Web de Orange County Lettings.
=====================================================================

En prérequis, d'un point de vue pratique vous aurez besoin de:
--------------------------------------------------------------
- un compte GitHub avec accès en lecture à ce repository
- une version Python, version 3.6 ou supérieure à installer(actuellement 3.12).
- installer Git, avec Git bash de préférence.
- créer un dossier dans lequel vous pourrez injecter le code hébergé sur GitHub.
- lancer ``git init`` depuis ce dossier.
- d'un environnement virtuel : ``python -m venv venv`` toujours depuis ce dossier. (cet environnement,
    permettra d'installer les packages et les dépendances nécéssaires au fonctionnement de l'application,
    tout en les isolants.)


Fork et clone de l'application.
-------------------------------
Rendez-vous sur: `https://github.com/lou57810/Clone-Python-OC-Lettings-FR`
Fork du projet pour créer un projet identique sur votre compte GitHub (Clic sur Fork et le nom du projet).
Donner un nom au projet forké, puis
clone du projet forké sur votre ordinateur local pour isoler le projet de l'original:
``git clone https://github.com/vote_id_git/nom_de_votre_projet_forké.git``
La commande ``ls`` affiche le nom du repositrory cloné sur notre poste de travail.

Lancement et test de l'application en local.
============================================
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

Elle est disponible en local à l'adresse: ``http://127.0.0.1:8000``

Vous avez également accès à l'administration:
Url: ``http://127.0.0.1:8000/admin``
Id: admin
Password: Abc1234!
