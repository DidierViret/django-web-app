# Django tutorial
Notes prises sur le cours OpenClassrooms

## Installation

### Création de l'environnement
Déplacement dans le dossier du projet et création d'un environnement virtuel

```shell
> cd <my_project_folder>
> python -m venv env
```

### Autorisation de l'exécution de scrpits sous Windows
Pour pouvoir exécuter les scrpits d'activation de l'environnement virtuel, il faut que Windows autorise l'exécution de scripts.
Les explications détaillées sont données dans cette documentation : [https://go.microsoft.com/fwlink/?LinkID=135170](https://go.microsoft.com/fwlink/?LinkID=135170)

Ouvrir une fenêtre Powershell en mode administrateur et exécuter la commande suivantes :

```shell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Activation de l'environnement sous Windows
Maintenant que l'exécution de scripts est autorisée, l'environnement virtuel peut être activé avec la commande suivante :

```shell
> .\env\Scripts\activate
(env) my_project_folder>
```
**Une fois l'environnement virtuel activé, l'invite de commande doit commencer par (env).**

### Installation de Django dans l'environnement virtuel
```shell
(env) > pip install django
```

Création d'un fichier pip "requirements.txt" qui liste les dépendance

```shell
(env) > pip freeze > requirements.txt
```

La commande pip install permet de réinstaller les mêmes dépendances dans d'autres environnements en se basant sur le fichier requirements.txt

```shell
(env) > pip install -r .\requirements.txt
```

### Initialisation d'un projet Django

Génération automatique du code de base Django (gabarit)
```shell
(env) > django-admin startproject <project-name>
```
Le fichier manage.py peut maintenant être utilisé pour lancer des commandes Django spécifiques au projet, à la place de la commande django-admin qui est plus générique.

### Démarrage du serveur de développement

```shell
(env) > python manage.py runserver
```

### Création de la base de données

```shell
(env) > python manage.py migrate
```

### Initialisation d'une application
Une application peut être comparée à un module du projet Django. Une application peut éventuellement être réutilisée dans plusieurs projets.

Création de l'application
```shell
(env) > python manage.py startapp <application-name>
```

L'application doit ensuite être mentionnée dans le fichier settings.py qui se trouve dans le répertoire du projet (le sous-répertoire qui porte le même nom que le répertoire principal).

Ajout de l'application dans INSTALLED_APPS du fichier settings.py
Création de l'application
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'listings',
]
```

## Migrations

### Générer un fichier de migration
Après avoir créé des modèles dans models.py, un fichier de migration peut être créé par une ligne de commande. Il contiendra toutes les modifications qui ont été trouvées dans models.py depuis le dernier fichier réalisé.

```shell
(env) > python manage.py makemigrations
```

### Exécuter les fichiers de migration pour les appliquer à la BD
Une fois le ou les fichiers de migration créés, les instructions peuvent être appliquées à la base de données afin de la créer ou la modifier.

```shell
(env) > python manage.py migrate
```
