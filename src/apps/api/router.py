# Setting for API Route
from rest_framework.routers import DefaultRouter

from apps.products.viewsets import ProductModelViewSet

router: DefaultRouter = DefaultRouter()


# register router here
router.register(r'products', ProductModelViewSet)
