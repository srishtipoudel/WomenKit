# WomenKit

**A project created by Team Lilacs for SheHacks 2021.**
**Find the site running on https://lilacs-womenkit.herokuapp.com/**
- 

### To setup virtual environment, run the following commands:
pipenv install

### To activate virtual environment run:
pipenv shell

### Installing django and djangorest framework:
```
pipenv install django
pipenv install djangorestframework
pipenv install psycopg2
pipenv install gunicorn
pipenv install django-heroku
```

### Lock pipfile:
```
pipenv lock
```
### Alternatively you can directly install everything from Pipfile.lock by running the command: 
```
pipenv install
```

---
### Install PostgreSQL
 _Install PostgreSQL (latest version) from https://www.postgresql.org/download/_

 _Setup postgres in your system according to your OS. Eg: for manjaro it would be something like this https://dev.to/tusharsadhwani/how-to-setup-postgresql-on-manjaro-linux-arch-412l_

 _Create a new database in your Postgres server and name it womenkit._
 ```
            create database womenkit;
            \c womenkit
  ```
---
## Edit Database configurations with your PostgreSQL configurations.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'womenkit',
        'USER': 'postgres',
        'PASSWORD': '<postgres-password>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
--- 
## Run the server

 ### Make migrations
 ```
  python manage.py makemigrations
  python manage.py migrate
 ```
 ### Run the server
  python manage.py runserver




