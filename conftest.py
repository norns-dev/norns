"""Configuration for pytest"""

import pytest

from accounts.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    """Media storage fixture"""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db):
    """User fixture"""
    return UserFactory()


@pytest.fixture()
def user2(db):
    """User fixture"""
    return UserFactory()
