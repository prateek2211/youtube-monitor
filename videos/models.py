from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    publish_time = models.DateTimeField()
    thumbnail = models.URLField()
    channel_title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-publish_time']