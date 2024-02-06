"""Views for parties app"""

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


class MemberGet(DetailView):
    """Returns member for party"""

    model = Party
    template_name = "party_detail.html"


class PartyDetailView(View):
    """View for party details"""

    def get(self, request, *args, **kwargs):
        """Returns details of party for GET methods"""
        view = MemberGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Returns details of party for POST methods"""
        view = MemberGet.as_view()
        return view(request, *args, **kwargs)


class PartyListView(ListView):
    """List of parties"""

    model = Party
    template_name = "party_list.html"
    ordering = ["name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted_at=None)


class PartyUpdateView(UpdateView):
    """Update parties view"""

    model = Party
    fields = ("description",)
    template_name = "party_edit.html"


class PartyDeleteView(DeleteView):
    """Delete parties view"""

    model = Party
    template_name = "party_delete.html"
    success_url = reverse_lazy("party_list")


class PartyCreateView(CreateView):
    """Create new party"""

    model = Party
    template_name = "party_new.html"
    fields = (
        "name",
        "description",
    )

    def form_valid(self, form):
        form.instance.dm = self.request.user
        return super().form_valid(form)
