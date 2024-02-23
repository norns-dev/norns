"""Accounts signals"""

from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import UserProfile


@receiver(user_signed_up)
def create_user_profile(user):
    """Creates user profile when a new user signs up"""
    UserProfile.objects.create(user=user)
