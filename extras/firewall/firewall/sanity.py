from celery import Celery

celery = Celery()

@celery.task
def task_sanity(x, y):
    # Task logic to process data
    return x + y