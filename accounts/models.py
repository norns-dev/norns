"""accounts models"""

import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user"""

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    # Custom fields
    location = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default="UTC")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    discord_username = models.CharField(max_length=50, null=True, blank=True)

    # Customized defaults
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="email address", unique=True
    )

    def __str__(self):
        return str(self.username)
