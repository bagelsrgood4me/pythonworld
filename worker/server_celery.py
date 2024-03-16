from celery import Celery

server_app  = Celery('server', broker='amqp://rabbitmq_container:5672', backend='redis://redis:6379/0')
server_app.autodiscover_tasks(packages=['myapp1', 'myapp2'], force=True)


# if __name__ == "__main__":
#     server_app.worker_main(argv=['worker', '-l', 'info', '-P', 'solo'])
