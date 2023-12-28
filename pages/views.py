"""
Views for pages app
"""

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home page"""

    template_name = "home.html"
