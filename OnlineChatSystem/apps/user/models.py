from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField("昵称", max_length=255)
    avatar = models.ImageField("头像", upload_to="users/avatar/%Y/%m", max_length=100,
                               default='img/avatar/default_avatar.jpg')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name