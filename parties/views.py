"""Views for parties app"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Party


class MemberGet(LoginRequiredMixin, DetailView):
    """Returns member for party"""

    model = Party
    template_name = "parties/party_detail.html"


class PartyDetailView(LoginRequiredMixin, View):
    """View for party details"""

    def get(self, request, *args, **kwargs):
        """Returns details of party for GET methods"""
        view = MemberGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Returns details of party for POST methods"""
        view = MemberGet.as_view()
        return view(request, *args, **kwargs)


class PartyListViewJoined(LoginRequiredMixin, ListView):
    """List of parties the user is a member in"""

    model = Party
    template_name = "parties/party_list_joined.html"
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted_at=None, partymember__user=self.request.user)


class PartyListViewOwned(LoginRequiredMixin, ListView):
    """List of parties the user is a member in"""

    model = Party
    template_name = "parties/party_list_owned.html"
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted_at=None, dm=self.request.user)


class PartyUpdateView(LoginRequiredMixin, UpdateView):
    """Update parties view"""

    model = Party
    fields = ("description",)
    template_name = "parties/party_edit.html"

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(dm=self.request.user)


class PartyDeleteView(LoginRequiredMixin, DeleteView):
    """Delete parties view"""

    model = Party
    template_name = "parties/party_delete.html"
    success_url = reverse_lazy("party_list")

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(dm=self.request.user)


class PartyCreateView(LoginRequiredMixin, CreateView):
    """Create new party"""

    model = Party
    template_name = "parties/party_new.html"
    fields = (
        "name",
        "description",
    )

    def form_valid(self, form):
        form.instance.dm = self.request.user
        return super().form_valid(form)
