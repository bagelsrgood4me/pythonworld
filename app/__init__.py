# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .client_celery import client_app

__all__ = ('client_app',)