Docker
======
Précédemment (page4) vous vous êtes enregistré sur dockehub, et avez installé docker en local.
Préalablement les fichier Dockerfile et .dockerignore (étapes inutiles à ignorer) sont déjà créés et figurent dans le code.
Rappel: Changer la valeur `dns` de votre acompte Sentry.

- création de l'image avec la commande suivante:
    ``docker build -t nom_de_votre_application . ``
    L'argument -t permet de donner un nom à votre image Docker.
    Cela permet de retrouver plus facilement l' image par la suite.
    Le . est le répertoire où se trouve le Dockerfile (c.a.d, à la racine du projet).
- lancement du container:
    ``docker run -d -p 8000:8000 nom_application`` (-p = port 8000:8000 pour Django)
    Le premier port est interne et le deuxième externe.
- Vous pouvez accèder à votre application en lancant dans le navigateur: http://127.0.0.1:8000


Docker Hub
----------
Pour l'instant, votre application est disponible en local, mais pouvez la rendre publique.
Pour rendre cette image publique,  il faut la publier sur Docker Hub, en lançant les commandes suivantes:
``docker tag ocr-docker-build:latest YOUR_USERNAME/nom_application:latest`` (Crée un lien entre l'image créée et
  l'image à envoyer.)
Puis:
``docker push YOUR_USERNAME/nom_application:latest``
Voilà, l'image figure sur une 'Registry' sur Docker Hub.