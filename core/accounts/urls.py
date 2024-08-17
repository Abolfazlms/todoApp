from django.urls import path
from .views import SignInView, SignUpView

from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("login/", SignInView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", SignUpView.as_view(), name="register"),
]
