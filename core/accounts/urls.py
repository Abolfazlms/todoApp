from django.urls import path
from .views import SignInView, SignUpView

from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
