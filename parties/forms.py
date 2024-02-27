"""Forms for parties app"""

from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Party, PartyMember


class PartyMemberForm(forms.ModelForm):
    """Form to add a party member"""

    class Meta:
        """Meta class."""

        model = PartyMember
        fields = ("user", "character_name")


class NewPartyForm(forms.ModelForm):
    """Form to add a party member"""

    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        """Meta class."""

        model = Party
        fields = ("name", "description")
