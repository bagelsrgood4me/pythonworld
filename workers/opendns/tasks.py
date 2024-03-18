from celery import shared_task


@shared_task
def block(x, y):
    # Task logic to process data
    return 5


@shared_task
def sanity(x, y):
    # Task logic to process data
    return 5


@shared_task
def validation(x, y):
    # Task logic to process data
    return 5
