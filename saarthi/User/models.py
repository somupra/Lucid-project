from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    saarthi = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    rewards = models.IntegerField()

