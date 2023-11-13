
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apps.api.router import router
from apps.products.urls import urlpatterns as product_urlpatterns

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint untuk mendapatkan token JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint untuk menyegarkan token JWT
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + product_urlpatterns  + router.urls 