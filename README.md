# Backend-Assignment
---
## Setup the project
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
## Run database migrations
```bash
python manage.py makemigrations
python manage,py migrate
```
## Create user
```bash
python manage.py createsuperuser
```

## Run server
```bash
python manage.py runserver
```