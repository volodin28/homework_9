# Homework #9

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/volodin28/homework_9
$ cd homework_9
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Run docker in terminal:

```sh
docker run -d -p 5672:5672 rabbitmq
```

Run worker:
```sh
celery -A homework_9 worker -l INFO
```

Once `pip` has finished downloading the dependencies and celery is working:
```sh
(env)$ cd homework_9
(env)$ python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/student/add/`