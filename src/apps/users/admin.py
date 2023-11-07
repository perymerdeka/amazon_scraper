from django.contrib import admin

from apps.users.models import UsersModel

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


admin.site.register(UsersModel, UserModelAdmin)