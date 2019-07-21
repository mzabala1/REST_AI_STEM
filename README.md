# REST_AI_STEM
Web application developed for STEM Skills project

## How to install and run app

> Step 1: Install requirements

```$ pip install -r requirements.txt```
> Step 2: make sure you have postgresql installed
> Create an user called "stemadmin"

```$ sudo -u postgres createuser --interactive```
> Step 3: Then set the password "stemadmin" to this user.

```ALTER USER stemadmin WITH PASSWORD 'stemadmin';```
> Step 4: Create a db called "STEMSkillsDB"
 
```$ createdb STEMSkillsDB```
> Step 5: Run server
```
$ python manage.py makemigrations STEM
$ python manage.py migrate
$ python manage.py runserver
```
> Step 6: Go to the webpage in your localhost

> http://127.0.0.1:8000/
