"""accounts admin"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, UserAdminCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Custom user admin"""

    add_form = UserAdminCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "location",
        "timezone",
        "first_name",
        "last_name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("location", "timezone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("location", "timezone")}),
    )
