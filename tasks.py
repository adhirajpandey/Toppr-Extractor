from celery import Celery
import time
from script import url_to_csv

#use sqlite db and sqlite broker
app = Celery('tasks', backend='db+sqlite:///db.sqlite', broker='sqla+sqlite:///db.sqlite')


@app.task
def url_to_csv_task(input_url):
    url_to_csv(input_url)

    return "out.csv"