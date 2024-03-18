from celery import Celery

celery = Celery()

@celery.task
def task_block(x, y):
    # Task logic to process data
    return x + y