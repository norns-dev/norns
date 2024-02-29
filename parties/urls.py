"""URLs for parties app"""

from django.urls import path

from .views import (
    PartyCreateView,
    PartyDeleteView,
    PartyDetailView,
    PartyListViewJoined,
    PartyListViewOwned,
    PartyUpdateView,
    RemoveMemberView,
)

urlpatterns = [
    path("member_remove/<int:pk>/", RemoveMemberView.as_view(), name="member_remove"),
    path("<int:pk>/delete/", PartyDeleteView.as_view(), name="party_delete"),
    path("<int:pk>/", PartyDetailView.as_view(), name="party_detail"),
    path("<int:pk>/edit/", PartyUpdateView.as_view(), name="party_edit"),
    path("joined/", PartyListViewJoined.as_view(), name="party_list_joined"),
    path("owned/", PartyListViewOwned.as_view(), name="party_list_owned"),
    path("new/", PartyCreateView.as_view(), name="party_new"),
    path("", PartyListViewJoined.as_view(), name="party_list_joined"),
]
