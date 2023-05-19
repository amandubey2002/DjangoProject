from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shopify.settings')

app = Celery('Shopify.settings')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')



app.conf.beat_schedule = {
        'add-every-1-seconds': {
        'task': 'frontapp.task.send_mail_to_user',
        'schedule':crontab(minute='*/60')
    },
}

app.conf.beat_schedule = {
        'delete-every-60-minutes': {
        'task': 'frontapp.task.permanent_delete_product',
        'schedule': crontab(minute=0, hour='*/1')
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"RequestL:{self.request!r}")


