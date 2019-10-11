from django.db import models
from user.models import User
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Room(models.Model):
    name = models.CharField("房间名", max_length=255)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    created_at = models.DateTimeField('更新时间', auto_now_add=True)
    #[{"user":user.id, "date":"2019-09-12 10:00:00"},]
    log_record = JSONField('日志', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='room_owner')
    user = models.ManyToManyField(User, verbose_name='用户', related_name='room_user')

    class Meta():
        verbose_name = '聊天室'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @property
    def room_users(self):
        return self.roomuser_set.all()