Render:
===================
- Création d'un compte. (Peut être lié avec GitHub pour le côté pratique)

- Renseigner quelques variables pour utiliser Render conjointement avec l'application stockée sur GitHub.
- Dans la rubrique Settings:
- Name: ``Nom de votre application clonée``
- Région: ``Frankfurt (EU Central)`` ou autre adresse proche.
- Dans Build & Deploy:
- Repository: ``Nom de votre repository`` ex: ``https://github.com/lou57810/Clone-Python-OC-Lettings-FR``
- Branch: 'main' 'master` ou autres.
- Deploy hook: (Render propose de la générer ou de la changer automatiquement.)
- Dans la rubrique Environnement:
- SECRET_KEY: La variable que nous avons copiée depuis le fichier à la racine: .env

- Une fois ces valeurs renseignées, Render vous communique l'adresse à utiliser en production sur la page ou figure votre
projet.