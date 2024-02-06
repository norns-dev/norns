"""accounts models"""

import pytz
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user"""

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    location = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default="UTC")
