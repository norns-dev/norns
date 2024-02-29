"""
Tests for party list joined page
"""

from allauth.account.models import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Party

User = get_user_model()


class PartyListJoinedPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser3", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(
            name="testparty", dm=cls.user, description="testdescription"
        )
        party.save()

        # Set reusable variables
        cls.abs_url = "/parties/joined/"
        cls.view_name = "party_list_joined"
        cls.expected_templates = [
            "base.html",
            "parties/party_list.html",
            "parties/party_list_joined.html",
        ]

    def setUp(self) -> None:
        # Logs the test user in
        self.client.force_login(self.user)

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
