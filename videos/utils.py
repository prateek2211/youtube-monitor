import requests
from videos.models import Video
from django.conf import settings
from rest_framework import status
from datetime import datetime


class Client(object):
    url = 'https://www.googleapis.com/youtube/v3/search'

    def fetch_and_save(self, after_timestamp):
        page_token = 'BEGIN'
        params = {
            'part': 'snippet',
            'maxResults': 50,
            'order': 'date',
            'q': settings.QUERY,
            'type': 'video',
            'pageToken': page_token,
            'key': settings.API_KEY,
            'publishedAfter': after_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        videos = []
        # get next page if page token available
        while page_token:
            if page_token == 'BEGIN':
                page_token = ''
            params['pageToken'] = page_token
            resp = requests.get(url=self.url, params=params, timeout=5, )
            print('Visiting page', resp.status_code)
            if resp.status_code == status.HTTP_200_OK:
                items = resp.json()['items']
                # check items as page token can be present even if no results after this page
                if 'nextPageToken' in resp.json() and items:
                    page_token = resp.json()['nextPageToken']
                else:
                    page_token = ''

                for item in items:
                    data = item['snippet']
                    # response is not correct if time is near to last upload video time
                    # check for incorrect response
                    if after_timestamp.replace(tzinfo=None) >= datetime.strptime(data['publishedAt'],
                                                                                 '%Y-%m-%dT%H:%M:%S.%fZ'):
                        page_token = ''
                        break
                    videos.append(Video(
                        title=data['title'],
                        description=data['description'],
                        publish_time=data['publishedAt'],
                        thumbnail=data['thumbnails']['default']['url'],
                        channel_title=data['channelTitle']
                    ))
        Video.objects.bulk_create(videos)

    def cron_job(self):
        last_record = Video.objects.values_list('publish_time').first()
        if last_record:
            last_record_time = last_record[0]
        else:
            last_record_time = datetime.strptime('2019-11-23T00:09:08.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')

        self.fetch_and_save(last_record_time)
