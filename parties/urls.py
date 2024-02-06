"""URLs for parties app"""

from django.urls import path

from .views import PartyDetailView

urlpatterns = [path("<int:pk>/", PartyDetailView.as_view(), name="party_detail")]
