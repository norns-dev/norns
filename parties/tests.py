"""
Tests for parties app
"""

from django.apps import apps
from django.test import TestCase
from django.urls import reverse

from .models import Party

User = apps.get_model("accounts", "CustomUser")


class PartyDetailPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(name="testparty", dm=cls.user)
        party.save()

        # Set reusable variables
        cls.test_obj_id = party.id
        cls.abs_url = f"/parties/{cls.test_obj_id}/"
        cls.view_name = "party_detail"
        cls.template_name = "parties/party_detail.html"

    def setUp(self) -> None:
        # Logs the test user in
        self.client.login(**self.user_params)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.abs_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_view_name(self):
        response = self.client.get(
            reverse(self.view_name, args=[self.test_obj_id]), follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, self.template_name)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.template_name)
