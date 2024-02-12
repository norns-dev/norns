"""accounts forms"""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """User creation form"""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = (
            "username",
            "email",
            "location",
            "timezone",
            "first_name",
            "last_name",
            "phone_number",
            "discord_username",
        )


class CustomUserChangeForm(UserChangeForm):
    """User change form"""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "location",
            "timezone",
            "email",
            "phone_number",
            "discord_username",
        )
