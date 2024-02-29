"""
Tests for party edit page
"""

from allauth.account.models import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Party

User = get_user_model()


class PartyEditPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser5", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test5@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(
            name="testparty", dm=cls.user, description="testdescription"
        )
        party.save()

        # Set reusable variables
        cls.test_obj_id = party.id
        cls.abs_url = f"/parties/{cls.test_obj_id}/edit/"
        cls.view_name = "party_edit"
        cls.expected_templates = ["base.html", "parties/party_edit.html"]

    def setUp(self) -> None:
        # Logs the test user in
        self.client.force_login(self.user)

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
        for template in self.expected_templates:
            self.assertTemplateUsed(response, template)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.expected_templates[-1])
