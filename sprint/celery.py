from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sprint.settings')

app = Celery('sprint')
app.conf.enable_utc = False


app.conf.update(timezone = 'America/Sao_Paulo')

app.config_from_object(settings, namespace = 'CELERY')

app.conf.beat_schedule = {
        'send-email-periodic': {
                'task' : 'send_email.tasks.send_email_func',
                'schedule': crontab(hour = 18, minute = 15, day_of_month = 5, month_of_year = 6)
                # 'args': 
        }
}
 
app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
        print(f'Request: {self.request!r}')