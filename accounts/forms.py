"""accounts forms"""

from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import UserProfile

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    """User change form for admin"""

    class Meta(admin_forms.UserChangeForm.Meta):
        """Meta class."""

        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        """Meta class."""

        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class UserProfileChangeForm(forms.ModelForm):
    """User change form"""

    class Meta:
        """Meta class."""

        model = UserProfile
        fields = (
            "location",
            "timezone",
            "phone_number",
            "discord_username",
        )
