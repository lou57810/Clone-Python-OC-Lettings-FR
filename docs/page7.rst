CircleCi
====================

Création d'un compte sur CircleCi. (Comme précédemment avec Render, utiliser le référencement GitHub, est très pratique.

- Pour profiter des retours de CircleCi il vous renseigner quelque indications
- et en particulier les variables d'environnement:
- DEBUG = False
- DEPLOY_HOOK = (valeur générée et figurant dans Render/Deployhook)
- DOCKER_HUB_PASSWORD = personal_password_hub (Le mien ou le vôtre)
- DOCKER_HUB_USER_ID = personal_user_id (Le mien ou le vôtre)
- SECRET_KEY = celui défini dans racine/.env
- dsn = celui défini dans racine/.env

- Circleci vérifie si les test existent et s'il réusissent.
- Création d'un fichier local pour les variables d'environnement.
- Configuration Django en mode production.
- Si vous utilisez Render comme solution de déploiement, veillez à désactiver le déploiement automatique à chaque commit.