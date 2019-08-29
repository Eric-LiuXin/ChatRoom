from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name