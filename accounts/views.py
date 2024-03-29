"""
Views for accounts app on norns
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .models import UserProfile


class UserProfileView(LoginRequiredMixin, DetailView):
    """User profile view"""

    model = UserProfile

    template_name = "registration/user_update_complete.html"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(id=self.request.user.id)


class UpdateUserView(UpdateView, LoginRequiredMixin):
    """Update user view"""

    model = UserProfile
    fields = (
        "location",
        "timezone",
        "phone_number",
        "discord_username",
    )
    template_name = "registration/user_update.html"
    success_url = reverse_lazy("user_update_complete", args=[1])

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(id=self.request.user.id)
