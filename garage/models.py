import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Vehicle(models.Model):
    CAR = 1
    MOTORCYCLE = 2
    ROLE_CHOICES = (
        (CAR, 'Car'),
        (MOTORCYCLE, 'Motorcycle'),
    )
    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year)]
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30)
    type = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    color = models.CharField(max_length=30)
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    price = models.PositiveIntegerField(blank=False, null=False)
    icon = models.ImageField()


