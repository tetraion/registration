from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('メールアドレス')

class UserUsageSituation(models.Model):
    # usage_situation_id = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    display_count = models.PositiveIntegerField(default=0)
    research_count = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.subject