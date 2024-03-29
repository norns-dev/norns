"""
Tests for parties app
"""

from allauth.account.models import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Party

User = get_user_model()


class PartyDetailPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser0", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test0@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(
            name="testparty", dm=cls.user, description="testdescription"
        )
        party.save()

        # Set reusable variables
        cls.test_obj_id = party.id
        cls.abs_url = f"/parties/{cls.test_obj_id}/"
        cls.view_name = "party_detail"
        cls.expected_templates = ["base.html", "parties/party_detail.html"]

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
        for template in self.expected_templates:
            self.assertTemplateUsed(response, template)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.expected_templates[-1])


class PartyListOwnedPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser1", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test1@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(
            name="testparty", dm=cls.user, description="testdescription"
        )
        party.save()

        # Set reusable variables
        cls.abs_url = f"/parties/owned/"
        cls.view_name = "party_list_owned"
        cls.expected_templates = [
            "base.html",
            "parties/party_list.html",
            "parties/party_list_owned.html",
        ]

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
        cls.abs_url = f"/parties/joined/"
        cls.view_name = "party_list_joined"
        cls.expected_templates = [
            "base.html",
            "parties/party_list.html",
            "parties/party_list_joined.html",
        ]

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
        for template in self.expected_templates:
            self.assertTemplateUsed(response, template)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.expected_templates[-1])


class PartyDeletePageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser6", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test6@localhost")
        super().setUpClass()

        # Create test Party
        party = Party.objects.create(
            name="testparty", dm=cls.user, description="testdescription"
        )
        party.save()

        # Set reusable variables
        cls.test_obj_id = party.id
        cls.abs_url = f"/parties/{cls.test_obj_id}/delete/"
        cls.view_name = "party_delete"
        cls.expected_templates = ["base.html", "parties/party_delete.html"]

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
        for template in self.expected_templates:
            self.assertTemplateUsed(response, template)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(self.abs_url, follow=True)
        self.assertTemplateNotUsed(response, self.expected_templates[-1])


class PartyNewPageTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create test user
        cls.user_params = {"username": "testuser7", "password": "testing123"}
        cls.user = User.objects.create_user(**cls.user_params, email="test7@localhost")
        super().setUpClass()

        # Set reusable variables
        cls.abs_url = f"/parties/new/"
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
