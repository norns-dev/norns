"""Views for parties app"""

from django.views import View
from django.views.generic import DetailView, ListView

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
