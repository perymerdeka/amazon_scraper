
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.api.router import router

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint untuk mendapatkan token JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint untuk menyegarkan token JWT
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + router.urls