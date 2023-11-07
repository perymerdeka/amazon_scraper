from rest_framework.viewsets import ModelViewSet

from apps.users.models import UsersModel
from apps.users.serializers import UserModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UserModelSerializer