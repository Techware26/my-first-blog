from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title