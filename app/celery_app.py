import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app',
                  broker='pyamqp://rabbitmq_container:5672',
                  backend='redis://redis:6379/0',
                  broker_connection_retry_on_startup=True,
                  task_reject_on_worker_lost=True,
                  task_acks_late=True,
                  result_backend_always_retry=True,
                  worker_deduplicate_successful_tasks=True,
                  worker_cancel_long_running_tasks_on_connection_loss=True,
                  worker_send_task_events=True,
                  task_send_sent_event=True
              )
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()