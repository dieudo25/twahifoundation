from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


class CustomUserAdmin(UserAdmin):
    """
    class UserAdmin definition
    """
    readonly_fields = ["slug"]

    fieldsets = (
        (None, {
            'classes': ('grp-collapse grp-closed'),
            "fields": (
                'username',
                'password',
                'avatar',
                'slug',
            ),
        }),
        ('Informations personelles', {
            "fields": (
                'first_name',
                'last_name',
                'email',
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
