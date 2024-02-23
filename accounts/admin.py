"""accounts admin"""

from django.contrib import admin

from .forms import UserAdminCreationForm, UserProfileChangeForm
from .models import UserProfile


@admin.register(UserProfile)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom user admin"""

    add_form = UserAdminCreationForm
    form = UserProfileChangeForm
    model = UserProfile
