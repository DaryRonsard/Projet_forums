Ce projet est une API REST qui permet de gérer un forum, des sujets (topics), et des messages. 
Il a été développé avec Django et Django REST Framework (DRF), en utilisant une base de données PostgreSQL.
                                                                                          
                                                                                          
    Prérequis

Python 3.12
Django 5.x ou supérieur
PostgreSQL installé et configuré
pip (gestionnaire de paquets Python)
Git (optionnel)

    Étapes d'installation

1. Cloner le projet (si applicable)
Si vous avez un dépôt Git, utilisez la commande suivante pour cloner le projet :

git clone https://github.com/HienDaryRonsard/projet_forums.git
si vous avez creer un dossier pour pouvoir mettre le projet dedans alors utiliser la commande ci dessous pour naviguer a l'interrieur du projet 
cd NomDossier

2. Créer et activer un environnement virtuel
   # Créer l'environnement virtuel
python -m venv env

# Activer l'environnement virtuel
.\env\Scripts\activate

3. Installer les dépendances
Installez les dépendances du projet, qui sont listées dans le fichier requirements.txt
naviguer vers le dossier src de notre projet
cd src ensuite tapé cette commande
# Installer les dépendances
pip install -r requirements.txt #pour installer les dépendance du projet

4. Configurer la base de données PostgreSQL
Créez une base de données PostgreSQL pour votre projet. Connectez-vous à PostgreSQL et exécutez la commande suivante pour créer une base de données :
CREATE DATABASE forum_db;


DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 'forum_db',
        
        'USER': 'votre_nom_utilisateur',
        
        'PASSWORD': 'votre_mot_de_passe',
        
        'HOST': 'localhost',
        
        'PORT': '5432',
        
    }
}

5. Appliquer les migrations
Après avoir configuré la base de données, appliquez les migrations pour créer les tables nécessaires.

python manage.py makemigrations
python manage.py migrate

7. Lancer le serveur de développement
Exécutez le serveur de développement pour démarrer l'API.

Vous pouvez maintenant accéder à l'API à l'adresse http://localhost:8000.
