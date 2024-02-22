from ..models import CustomUser


def test_user_get_absolute_url(user: CustomUser):
    assert user.get_absolute_url() == f"/users/{user.username}/"
