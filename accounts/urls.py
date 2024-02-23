"""accounts URL Configuration"""

from django.urls import path

from .views import UpdateUserView, UserProfileView

urlpatterns = [
    path("<int:pk>/edit/", UpdateUserView.as_view(), name="update_user"),
    path("<int:pk>/", UserProfileView.as_view(), name="user_update_complete"),
]
