"""URLs for parties app"""

from django.urls import path

from .views import PartyDetailView, PartyListView

urlpatterns = [
    path("<int:pk>/", PartyDetailView.as_view(), name="party_detail"),
    path("", PartyListView.as_view(), name="party_list"),
]
