from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from apps.users.models import UsersModel
from apps.users.serializers import UserModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UserModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = RefreshToken.for_user(user)  # Mendapatkan token refresh
        access_token = str(refresh.access_token)  # Mendapatkan token akses
        response_data = {
            'access_token': access_token,
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }
        return Response(response_data)

    def perform_create(self, serializer):
        return serializer.save()