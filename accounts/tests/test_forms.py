"""Module for all Form Tests."""

from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from ..forms import UserAdminCreationForm
from ..models import CustomUser


class TestUserAdminCreationForm(TestCase):
    """
    Test class for all tests related to the UserAdminCreationForm
    """

    def test_username_validation_error_msg(self, user: CustomUser):
        """
        Tests UserAdminCreation Form's unique validator functions correctly by testing:
            1) A new user with an existing username cannot be added.
            2) Only 1 error is raised by the UserCreation Form
            3) The desired error message is raised
        """

        # The user already exists,
        # hence cannot be created.
        form = UserAdminCreationForm(
            {
                "username": user.username,
                "password1": user.password,
                "password2": user.password,
            },
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertIn("username", form.errors)
        self.assertEqual(
            form.errors["username"][0], _("This username has already been taken.")
        )
