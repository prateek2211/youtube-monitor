from django.urls import path
from videos.views import *

urlpatterns = [
    path('videos/', VideoList.as_view(), name='videos'),
]
