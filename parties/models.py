"""Models for parties app"""

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from markdownx.models import MarkdownxField


class SoftDeleteQuerySet(models.query.QuerySet):
    """Custom queryset for soft deleted objects"""

    def delete(self):
        """Soft deletes an object. i.e. sets deleted_at to current timestamp"""
        return super().update(deletd_at=now())

    def hard_delete(self):
        """Hard deletes an object. i.e. removes the record from the database"""
        return super().delete()

    def active(self):
        """Returns only active objects"""
        return self.filter(deleted_at=None)

    def inactive(self):
        """Returns only inactive objects"""
        return self.exclude(deleted_at=None)


class SoftDeleteManager(models.Manager):
    """Manager for soft deletion of objects"""

    def __init__(self, *args, **kwargs):
        self.active_only = kwargs.pop("active_only", True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        """Custom queryset for soft deleted objects"""
        if self.active_only:
            return SoftDeleteQuerySet(self.model).filter(deleted_at=None)
        return SoftDeleteQuerySet(self.model)

    def hard_delete(self):
        """Queryset for hard deletion of objects"""
        return self.get_queryset().hard_delete()


class SoftDeleteModel(models.Model):
    """Base model for objects that require soft deletion"""

    deleted_at = models.DateTimeField(null=True, blank=True)

    all_objects = SoftDeleteManager(active_only=False)
    objects = SoftDeleteManager()

    class Meta:
        """Sets model as abstract"""

        abstract = True

    def delete(self, *args, **kwargs):
        """Soft deletes object by setting deleted_at to the current timestamp"""
        self.deleted_at = now()
        self.save(*args, **kwargs)

    def hard_delete(self, *args, **kwargs):
        """Hard deletes an object from the database"""
        super().delete(*args, **kwargs)


class Party(SoftDeleteModel):
    """Party model"""

    name = models.CharField(max_length=100)
    description = MarkdownxField(null=True, blank=True)
    dm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        verbose_name_plural = "Parties"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Returns absolute URL for parties detail view"""
        return reverse("party_detail", kwargs={"pk": self.pk})


class PartyMember(SoftDeleteModel):
    """Member model"""

    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    character_name = models.CharField(max_length=100, default="name")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.party.name + " - " + str(self.user) + " - " + self.character_name

    def get_absolute_url(self):
        """Returns absolute URL for party members detail view"""
        return reverse("party_member_detail", kwargs={"pk": self.pk})
