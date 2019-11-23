from celery.task import periodic_task
from videos.utils import Client

c = Client()


@periodic_task(run_every=20)
def fetch_job():
    print('Making API requests')
    c.cron_job()
