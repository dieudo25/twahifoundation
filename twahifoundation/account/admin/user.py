from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from account.models import User


class CustomUserResource(resources.ModelResource):
    """Describe how User resources can be imported or exported"""

    class Meta:
        """Meta definition for CustomUserResource."""

        model = User
        skip_unchanged = True


class CustomUserAdmin(ImportExportModelAdmin):
    """
    class UserAdmin definition
    """
    readonly_fields = ["slug"]
    resource_class = CustomUserResource

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
