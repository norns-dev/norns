"""accounts models"""

import pytz
from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """Custom user"""

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    location = models.CharField(max_length=50, null=True, blank=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default="UTC")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    discord_username = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)
