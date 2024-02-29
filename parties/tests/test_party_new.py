"""
Tests for party_new page
"""

from allauth.account.models import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class PartyNewPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser7", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test7@localhost")
        super().setUpClass()

        # Set reusable variables
        cls.abs_url = "/parties/new/"
        cls.view_name = "party_new"
        cls.expected_templates = ["base.html", "parties/party_new.html"]

    def setUp(self) -> None:
        # Logs the test user in
        self.client.login(**self.user_params)

    def test_url_exists_at_correct_location(self):
        response = self.client.get(self.abs_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_view_name(self):
        response = self.client.get(reverse(self.view_name), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(self.abs_url, follow=True)
        for template in self.expected_templates:
            self.assertTemplateUsed(response, template)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.expected_templates[-1])
