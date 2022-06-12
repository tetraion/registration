from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('メールアドレス')

class Hiragana(models.Model):
    moji = models.CharField('平文字', max_length=50)

    def __str__(self):
        return self.moji
