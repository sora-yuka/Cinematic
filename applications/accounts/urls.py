from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from applications.accounts.views import (UserRegistrationApiView, UserActivationApiView
)


urlpatterns = [
    path('register/', UserRegistrationApiView.as_view()),
    path('activate/<uuid:activation_code>/', UserActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]

