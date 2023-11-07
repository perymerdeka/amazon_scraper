from rest_framework.serializers import ModelSerializer

from apps.users.models import UsersModel

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['email', 'phone_number', 'name']