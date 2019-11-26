from celery.task import periodic_task
from celery.schedules import crontab
from videos.utils import Client
from videos.models import Video
from django.conf import settings

c = Client()


@periodic_task(run_every=settings.TIME_INTERVAL)
def fetch_job():
    print('Making API requests')
    c.cron_job()


# delete last 20 records every hour
@periodic_task(run_every=crontab(hour='*', minute=1))
def clean_database():
    Video.objects.reverse()[:20].delete()
