import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

client_app = Celery('server')
client_app.config_from_object('django.conf:settings', namespace='CELERY')


# @client_app.task(name='proxy.block.task_block')
# def proxy_block(x,y):
#     pass
#
# @client_app.task(name='proxy.sanity.task_sanity')
# def proxy_sanity(x,y):
#     pass
#
# @client_app.task(name='proxy.validation.task_validation')
# def proxy_validation(x,y):
#     pass
#
# @client_app.task(name='firewall.block.block')
# def firewall_block(x,y):
#     pass
#
# @client_app.task(name='firewall.sanity.sanity')
# def firewall_sanity(x,y):
#     pass
#
# @client_app.task(name='firewall.validation.validation')
# def firewall_validation(x,y):
#     pass
#
# @client_app.task(name='opendns.block.task_block')
# def opendns_block(x,y):
#     pass
#
# @client_app.task(name='opendns.sanity.task_sanity')
# def opendns_sanity(x,y):
#     pass
#
# @client_app.task(name='opendns.validation.task_validation')
# def opendns_validation(x,y):
#     pass
