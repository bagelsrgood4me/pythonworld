from celery import Celery

app = Celery('worker',
  broker='pyamqp://rabbitmq_container:5672',
  backend='redis://redis:6379/0',
  broker_connection_retry_on_startup=True,
  task_reject_on_worker_lost=True,
  task_acks_late=True,
  result_backend_always_retry=True,
  worker_deduplicate_successful_tasks=True,
  worker_cancel_long_running_tasks_on_connection_loss=True,
  worker_send_task_events=True,
  task_send_sent_event=True,
  task_routes = {
    "opendns.tasks.block": {'queue': 'block'},
    "opendns.tasks.validation": {'queue': 'validation'},
    "opendns.tasks.sanity": {'queue': 'sanity'},
  }
)

app.autodiscover_tasks(packages=['opendns'], force=True)

assert app.tasks['opendns.tasks.block']
assert app.tasks['opendns.tasks.sanity']
assert app.tasks['opendns.tasks.validation']