import contextlib
from http import HTTPStatus
from importlib import reload

import pytest
from django.contrib import admin
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse

from ..models import CustomUser


class TestUserAdmin(TestCase):
    def test_changelist(self, admin_client):
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_search(self, admin_client):
        url = reverse("admin:users_user_changelist")
        response = admin_client.get(url, data={"q": "test"})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_add(self, admin_client):
        url = reverse("admin:users_user_add")
        response = admin_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = admin_client.post(
            url,
            data={
                "username": "test",
                "password1": "My_R@ndom-P@ssw0rd",
                "password2": "My_R@ndom-P@ssw0rd",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(CustomUser.objects.filter(username="test").exists())

    def test_view_user(self, admin_client):
        user = CustomUser.objects.get(username="admin")
        url = reverse("admin:users_user_change", kwargs={"object_id": user.pk})
        response = admin_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @pytest.fixture()
    def _force_allauth(self, settings):
        settings.DJANGO_ADMIN_FORCE_ALLAUTH = True
        # Reload the admin module to apply the setting change
        import accounts.admin as users_admin

        with contextlib.suppress(admin.sites.AlreadyRegistered):
            reload(users_admin)

    @pytest.mark.django_db()
    @pytest.mark.usefixtures("_force_allauth")
    def test_allauth_login(self, rf, settings):
        request = rf.get("/fake-url")
        request.user = AnonymousUser()
        response = admin.site.login(request)

        # The `admin` login view should redirect to the `allauth` login view
        target_url = reverse(settings.LOGIN_URL) + "?next=" + request.path
        self.assertRedirects(response, target_url, fetch_redirect_response=False)
