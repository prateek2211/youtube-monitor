from rest_framework.serializers import ModelSerializer
from videos.models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
