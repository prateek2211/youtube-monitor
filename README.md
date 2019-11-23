# Backend-Assignment
---
## Setup Instructions
* Setup virtual environment
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
* Install RabbitMQ
```bash
sudo apt install rabbitmq-server
```

* Run database migrations
```bash
python manage.py makemigrations
python manage,py migrate
```
* Create superuser
```bash
python manage.py createsuperuser
```
* Start celery worker process
```bash
celery -A conf worker -B
```

* To run server open new terminal and enter the following command: 
```bash
python manage.py runserver
```
**Now open the browser and visit [this](http://127.0.0.1:8000/api/videos/) link to browse API**