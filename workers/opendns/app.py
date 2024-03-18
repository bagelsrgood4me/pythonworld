from celery import Celery

app = Celery(main='server',
             broker='pyamqp://rabbitmq_container:5672',
             backend='rpc://',
             broker_connection_retry_on_startup=True)

app.autodiscover_tasks(packages=['opendns'], force=True)

assert app.tasks['opendns.tasks.block']
assert app.tasks['opendns.tasks.sanity']
assert app.tasks['opendns.tasks.validation']