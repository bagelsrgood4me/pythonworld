from celery import Celery
from proxy import block, validation, sanity

app = Celery(main='server',
             broker='pyamqp://rabbitmq_container:5672',
             backend='redis://redis:6379/0',
             broker_connection_retry_on_startup=True)