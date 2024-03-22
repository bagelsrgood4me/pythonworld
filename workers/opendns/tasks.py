from celery import shared_task
from .helper import sum

@shared_task
def block(x, y):
    # Task logic to process data
    return sum(x,y)


@shared_task
def sanity(x, y):
    # Task logic to process data
    return sum(x, y)

@shared_task
def validation(x, y):
    # Task logic to process data
    return sum(x, y)


@shared_task
def on_chord_success(results):
    # This function will be called when all tasks in the chord complete successfully
    print("All tasks completed successfully")
    return results