from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=False)
    balance = models.PositiveIntegerField(default=100000, blank=False, null=False)

