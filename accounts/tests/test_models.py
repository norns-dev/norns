from django.test import SimpleTestCase

from ..models import CustomUser


class TestAccountsModels(SimpleTestCase):
    def test_user_get_absolute_url(self, user: CustomUser):
        self.assertEqual(user.get_absolute_url(), f"/users/{user.username}/")
