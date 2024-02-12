"""
URL configuration for norns project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("mstr/", admin.site.urls, name="admin"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("parties/", include("parties.urls")),
    path("", include("pages.urls")),
]
