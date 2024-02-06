"""Models for parties app"""

from django.conf import settings
from django.db import models
from django.urls import reverse


class Party(models.Model):
    """Party model"""

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    dm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Meta class."""

        verbose_name_plural = "Parties"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Returns absolute URL for parties detail view"""
        return reverse("party_detail", kwargs={"pk": self.pk})


class PartyMember(models.Model):
    """Member model"""

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    character_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.party.name + " - " + str(self.user) + " - " + self.character_name

    def get_absolute_url(self):
        """Returns absolute URL for party members detail view"""
        return reverse("party_member_detail", kwargs={"pk": self.pk})
