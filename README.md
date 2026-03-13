# Application Streamlit

Application réalisée pour le TP3.

Fonctionnalités :
- exploration des données
- entraînement d'un modèle
- prédiction

## Déploiement

L'application a été développée en Python avec **Streamlit** puis déployée sur **Streamlit Community Cloud**.

Le code du projet a été publié sur GitHub :

https://github.com/Josef1502/streamlit-tp3

L'application est accessible en ligne à l'adresse suivante :

https://app-tp3-cakmwpwbd2u5ve6q63dypn.streamlit.app/

Le déploiement a été réalisé en connectant le dépôt GitHub à Streamlit Cloud, qui installe automatiquement les dépendances définies dans le fichier `requirements.txt` et lance l'application.

## Sécurité

Plusieurs éléments de sécurité ont été mis en place :

- L'application est accessible via **HTTPS**, garantissant une connexion sécurisée (présence du cadenas 🔒 dans le navigateur).
- Une **authentification basique par mot de passe** a été ajoutée pour limiter l'accès à l'application.
- Les **entrées utilisateur sont validées** afin d'éviter des valeurs incorrectes.
- Des **logs** ont été ajoutés pour suivre l'exécution de l'application.

Avec 
- Un mot de passe : tp3_mbg
- Un lien Stremlit : https://app-tp3-cakmwpwbd2u5ve6q63dypn.streamlit.app/Training
- Une sécurisation HTPPS : OUI
- Une Utilisation de Github
- Un jeu de données à intégrer
- Un fichier log