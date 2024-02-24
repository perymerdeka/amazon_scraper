# Setting for API Route
from rest_framework.routers import DefaultRouter

from apps.products.viewsets import ProductModelViewSet
from apps.users.viewsets import UserModelViewSet

router: DefaultRouter = DefaultRouter()


# register router here
router.register(r'products', ProductModelViewSet, basename="product")
router.register(r'users', UserModelViewSet, basename='user')
