from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)  # 제목
    content = models.TextField()  # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.title