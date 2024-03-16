from celery import shared_task

@shared_task()
def worker_task(x, y):
    result = x + y
    return result