Déploiement
===============
Mise en place du déploiement avec Docker, et le pipleline Cicd:
---------------------------------------------------------------
Plusieurs étapes seront nécéssaires pour le déploiement de notre application:
- Gunicorn
- Docker
- CircleCi (Ci/Cd)
- Render

Gunicorn:
---------
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server Web for UNIX.
Gunicorn joue le rôle d'un serveur web(adapté au langage Python), comme par exemple Apache ou Nginx,
mais en version légère.
Cette fonction est renseignée dans le Dockerfile:
``CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]``

Docker:
------
Création d'un container et d'une image pour l' application.
Tout d'abord, installer Docker en local, et s'enregistrer sur Docker Hub.
Le Dockerfile est déjà implémenté dans le dossier racine, néanmoins vous devez renseigner votre propre dns Sentry.
Dockerfile décrit l'ensemble des étapes à réaliser pour pouvoir lancer votre nouvelle application.
Chaque instruction que vous allez donner dans votre Dockerfile va créer une nouvelle layer,
correspondant à chaque étape de la construction de l'image.
Comme exemple, à la base:
``# base image
FROM python:3.12``

Render:
-------
Render est une plateforme populaire pour le déploiement de pages web et d’applications.
Docker pour le stockage de notre application, Gunicorn comme Server Web, mais,
pour le moment, il manque un hébergeur.
C'est ici que Render rentre en fonction pour la diffusion de l'application sur la toile.

CircleCi:
---------
CircleCi est l'outil manquant au développement de notre application:
CircleCi permet de tester chaque commit réalisé avec git, et remonter les informations de défaillance ou de succès.

