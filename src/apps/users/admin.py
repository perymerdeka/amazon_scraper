from django.contrib import admin

from apps.users.models import UsersModel

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(UsersModel, UserModelAdmin)