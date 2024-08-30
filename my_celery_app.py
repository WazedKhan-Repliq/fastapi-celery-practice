import time
from celery import Celery

# Create a Celery instance
app = Celery('my_celery_app', broker='redis://localhost:6379/0')

# task to simply print hello world
@app.task
def hello_world()-> str:
    return "Hello World"


@app.task
def hello_earth()-> str:
    print("sleeping for a min")
    time.sleep(5)
    return "Hello Earth!"
