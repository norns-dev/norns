"""accounts apps"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Accounts config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        """Readies signals"""
        import accounts.signals

        _ = accounts.signals
