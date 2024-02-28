"""
URL configuration for norns project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin
    path("mstr/", admin.site.urls, name="admin"),
    # 3rd Party
    path("accounts/", include("allauth.urls")),
    path("markdownx/", include("markdownx.urls")),
    # Local
    path("accounts/", include("accounts.urls")),
    path("parties/", include("parties.urls")),
    path("", include("pages.urls")),
]
