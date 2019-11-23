# Backend-Assignment
---
## Setup Instructions
* Clone the repository
```bash
$ git clone https://github.com/prateek2211/backend-assignment.git
$ cd backend-assignment
```
* Setup virtual environment
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
*RabbitMQ is used as message broker to manage messages via queques for background process*
* Install RabbitMQ
```bash
$ sudo apt install rabbitmq-server
```
* Verify that RabbitMQ is running
```bash
$ sudo systemctl status rabbitmq-server
```
* **Next enter your API key in settings.py**. To get an API key visit [here](https://console.developers.google.com/apis)
* Run database migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
* Create superuser
```bash
$ python manage.py createsuperuser
```
* Start celery worker process
```bash
$ celery -A conf worker -B
```

* To run server open new terminal and enter the following command: 
```bash
$ python manage.py runserver
```
**Now open the browser and visit [this](http://127.0.0.1:8000/api/videos/) link to browse API**