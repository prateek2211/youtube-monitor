from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
