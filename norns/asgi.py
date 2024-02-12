"""
ASGI config for norns project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "norns.settings")

application = get_asgi_application()
