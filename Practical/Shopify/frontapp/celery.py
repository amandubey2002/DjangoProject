from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings



# from django.conf import settings
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shopify.settings')

app = Celery('Shopify.settings')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')


#Celery beat settings
# CELERY_BEAT_SCHEDULE = {
#       'add-every-30-seconds': {
#         'task': 'frontapp.tasks.send_mail_to_user',
#         'schedule': 30.0,
#     },
# }


app.conf.beat_schedule = {
        'add-every-1-seconds': {
        'task': 'frontapp.task.send_mail_to_user',
        'schedule':crontab(minute='*/1')
    },
}

app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Hello from Celery')




@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


