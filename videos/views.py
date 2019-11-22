from rest_framework.response import Response
from rest_framework.views import APIView

from videos.models import Video
from videos.serializers import VideoSerializer


class VideoList(APIView):
    def get(self, request):
        problems = Video.objects.all()
        serializer = VideoSerializer(problems, many=True)
        return Response(serializer.data)
