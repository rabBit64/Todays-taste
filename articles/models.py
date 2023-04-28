from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(blank=True, null=True,
                                upload_to='img/',
                                processors=[ResizeToFill(260, 300)],
                                format='JPEG',
                                options={'quality': 90})
    # deadline = models.DateTimeField(auto_now=True)
    # 시간 설정
    def time_since_created(self):
        time_difference = timezone.now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60
        if days >= 1:
            return '{}일 전'.format(days)
        elif hours >= 1:
            return '{}시간 전'.format(hours)
        elif minutes >= 1:
            return " {}분 전".format(minutes)
        else:
            return '방금 전'


    
    
  


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def time_since_created(self):
        time_difference = timezone.now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60
        if days >= 1:
            return '{}일'.format(days)
        elif hours >= 1:
            return '{}시간'.format(hours)
        elif minutes >= 1:
            return " {}분".format(minutes)
        else:
            return '방금 '
    
