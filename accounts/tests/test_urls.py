from django.test import TestCase
from django.urls import resolve, reverse

from ..models import CustomUser


class TestAccountsUrls(TestCase):
    def test_detail(self, user: CustomUser):
        self.assertEqual(
            reverse("users:detail", kwargs={"username": user.username}),
            f"/users/{user.username}/",
        )
        self.assertEqual(resolve(f"/users/{user.username}/").view_name, "users:detail")

    def test_update(self):
        self.assertEqual(reverse("users:update"), "/users/~update/")
        self.assertEqual(resolve("/users/~update/").view_name, "users:update")

    def test_redirect(self):
        self.assertEqual(reverse("users:redirect"), "/users/~redirect/")
        self.assertEqual(resolve("/users/~redirect/").view_name, "users:redirect")
