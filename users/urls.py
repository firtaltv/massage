from django.urls import path
from .views import UserProfileAPIView, LoginAPIView

app_name = "users"

urlpatterns = [
    path('', UserProfileAPIView.as_view(), name='user_profile'),
    path("login/", LoginAPIView.as_view(), name="login"),
]
