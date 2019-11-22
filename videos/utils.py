import requests
from videos.models import Video
from django.conf import settings
from rest_framework import status
from datetime import datetime


class Client(object):
    url = 'https://www.googleapis.com/youtube/v3/search'

    def __init__(self, username, password):
        self.username, self.password = username, password

    def fetch(self, after_timestamp):
        page_token = 'BEGIN'
        params = {
            'part': 'snippet',
            'maxResults': 25,
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
            resp = requests.get(url=self.url, params=params, timeout=1, )
            print('Visiting token', resp.request.params['pageToken'])
            if resp.status_code == status.HTTP_200_OK:
                if 'nextPageToken' in resp.json():
                    page_token = resp.json()['nextPageToken']
                else:
                    page_token = ''
                items = resp.json()['items']

                for item in items:
                    data = item['snippet']
                    # response is not correct if time is near to last upload video time
                    # check for incorrect response
                    if after_timestamp > datetime.strptime(data['publishedAt'], '%Y-%m-%dT%H:%M:%S.%fZ'):
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

# 2019-11-22T21:50:37Z
# 2019-11-22T22:50:37Z
