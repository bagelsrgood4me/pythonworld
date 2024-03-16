import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

client_app = Celery('client')

client_app.config_from_object('django.conf:settings', namespace='CELERY')
