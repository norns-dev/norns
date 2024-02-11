"""Admin for parties app"""

from django.contrib import admin

from .models import Party, PartyMember


class PartyMemberInLine(admin.TabularInline):
    """Tabular Inline for party members"""

    model = PartyMember
    extra = 0


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    """Admin for parties"""

    inlines = [PartyMemberInLine]
    list_display = ["name"]


admin.site.register(PartyMember)
