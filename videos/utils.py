import requests
from videos.models import Video
from django.conf import settings


class Client(object):
    url = 'https://www.googleapis.com/youtube/v3/search'

    def __init__(self, username, password):
        self.username, self.password = username, password

    def fetch(self, after_timestamp):
        resp = requests.get(url=self.url, params={
            'part': 'snippet',
            'maxResults': 25,
            'order': 'date',
            'q': settings.QUERY,
            'type': 'video',
            'key': settings.API_KEY,
            'publishedAfter': after_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        }, headers={}, timeout=1, )
        items = resp.json()['items']
        videos = []
        for item in items:
            data = item['snippet']
            videos += Video(
                title=data['title'],
                description=data['description'],
                publish_time=data['publishedAt'],
                thumbnail=data['thumbnails']['default']['url'],
                channel_title=data['channelTitle']
            )
        Video.objects.bulk_create(videos)
