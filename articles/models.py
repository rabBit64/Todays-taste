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
    # 스크랩
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='scrapped_articles')
    # 조회수
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = ProcessedImageField(blank=True, null=True,
    #                             upload_to='img/',
    #                             processors=[ResizeToFill(260, 300)],
    #                             format='JPEG',
    #                             options={'quality': 90})
    image = models.ImageField(upload_to='article_img/',blank=True, null=True,)
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


# 상품 모델
class Product(models.Model):
    product_name = models.TextField() #상품명
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=15)
    main_image = models.ImageField(upload_to='product/')
    content = models.TextField() #상품정보
    scrap = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='scrapped_product',null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_product',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# 상품 다중 이미지
class ProductImages(models.Model):
    product = models.ForeignKey(Product,blank=False,null=False,on_delete=models.CASCADE)
    photo = ProcessedImageField(blank=True, null=True,
                                upload_to='product/',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 90},)


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
    
