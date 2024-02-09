"""Forms for parties app"""

from django import forms

from .models import PartyMember


class PartyMemberForm(forms.ModelForm):
    """Form to add a party member"""

    class Meta:
        """Meta class."""

        model = PartyMember
        fields = ("user", "character_name")
