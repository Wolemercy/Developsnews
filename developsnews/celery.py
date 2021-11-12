import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'developsnews.settings')

app = Celery('developsnews')
# app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'refresh_votes': {
        "task": "api.tasks.refresh_votes",
        "schedule": crontab(minute='*/1')
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')