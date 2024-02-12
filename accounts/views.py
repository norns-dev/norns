"""
Views for accounts app on norns
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    """Sign up view for norns"""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserProfileView(LoginRequiredMixin, DetailView):
    """User profile view"""

    model = CustomUser

    template_name = "registration/user_update_complete.html"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(id=self.request.user.id)


class UpdateUserView(UpdateView, LoginRequiredMixin):
    """Update user view"""

    model = CustomUser
    fields = (
        "first_name",
        "last_name",
        "location",
        "timezone",
        "email",
        "phone_number",
        "discord_username",
    )
    template_name = "registration/user_update.html"
    success_url = reverse_lazy("user_update_complete", args=[1])

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(id=self.request.user.id)
