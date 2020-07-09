from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


class CustomUserAdmin(UserAdmin):
    """
    class UserAdmin definition
    """

    fieldsets = (
        (None, {
            'classes': ('grp-collapse grp-closed'),
            "fields": (
                'username',
                'password',
                'avatar',
            ),
        }),
        ('Informations personelles', {
            "fields": (
                'first_name',
                'last_name',
                'language',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Dates importantes', {
            "fields": (
                'last_login',
                'date_joined'
            ),
        }),
    )


admin.site.register(User, CustomUserAdmin)
