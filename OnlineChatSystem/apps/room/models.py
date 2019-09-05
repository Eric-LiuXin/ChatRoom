from django.db import models
from users.models import User
# Create your models here.

class Room(models.Model):
    name = models.CharField("房间名", max_length=255)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    created_at = models.DateTimeField('更新时间', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
