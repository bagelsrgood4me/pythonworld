from celery import shared_task
from .models import Block
from django.core import serializers
@shared_task
def add(x, y):
    total = x + y
    update.apply_async(total)


@shared_task
def update(results):
    # This function will be called when all tasks in the chord complete successfully
    print("Creating record")
    total = sum(results)
    print("Total:", total)
    block = Block.objects.create(name='test', status='test', code=total)
    return serializers.serialize('json', [block,])

@shared_task
def on_chord_success(results):
    # This function will be called when all tasks in the chord complete successfully
    print("All tasks completed successfully")
    return results

@shared_task
def on_chord_error(request, exc, traceback):
    # This function will be called if any task in the chord fails
    return f"Error occurred during chord execution: {exc}:{traceback}"