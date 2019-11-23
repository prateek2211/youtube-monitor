from rest_framework.generics import ListAPIView

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
