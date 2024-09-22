from django.urls import path, include
from .views import SignInView, SignUpView

from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("logout", LogoutView.as_view(next_page="signin/"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("api/v1/", include("accounts.api.v1.urls")),
]
