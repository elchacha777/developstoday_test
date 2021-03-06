from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from account.views import RegistrationView

urlpatterns = [
    path("register/", RegistrationView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
