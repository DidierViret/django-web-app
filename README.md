# Django tutorial
Notes prises sur le cours OpenClassrooms

## Installation
Déplacement dans le dossier du projet et installation d'un environnement virtuel

```shell
> cd <my_project_folder>
> python -m venv env
```

Activation de l'environnement virtuel (sous Windows). Attention, il faut que Windows autorise l'exécution de script, voir cette documentation : [https://go.microsoft.com/fwlink/?LinkID=135170](https://go.microsoft.com/fwlink/?LinkID=135170)

```shell
> .\env\Scripts\activate
(env) my_project_folder>
```
**Une fois l'environnement virtuel activé, l'invite de commande doit commencer par (env).**

Installation de Django dans l'environnement virtuel

```shell
(env) > pip install django
```

Création d'un fichier pip "requirements.txt" qui liste les dépendance

```shell
> pip freeze > requirements.txt
```

## Initialisation d'un projet Django

Génération automatique du code de base Django (gabarit)
```shell
(env) > django-admin startproject <project-name>
```
Le fichier manage.py peut maintenant être utilisé pour lancer des commandes Django spécifiques au projet, à la place de la commande django-admin qui est plus générique.

## Démarrage du serveur de développement

```shell
(env) > python manage.py runserver
```

## Création de la base de données

```shell
(env) > python manage.py migrate
```