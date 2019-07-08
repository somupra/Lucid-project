from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_official = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rewards = models.IntegerField(default = 0)
    spamcount = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.user.username} Profile'
