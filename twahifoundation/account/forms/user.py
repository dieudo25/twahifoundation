from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models.user import User


class UserCreateForm(UserCreationForm):
    """UserCreateForm custom made class"""

    class Meta:
        """Meta definition of UserCreateForm"""

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class UserUpdateForm(UserChangeForm):
    """UserCreateForm custom made class"""

    class Meta:
        """Meta definition of UserCreateForm"""

        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'language',
            'avatar',
            'password',
        ]


class UserGroupUpdateForm(forms.ModelForm):
    """UserCreateForm custom made class"""

    class Meta:
        """Meta definition of UserCreateForm"""

        model = User
        fields = [
            'groups'
        ]
        widgets = {
            'groups': forms.widgets.CheckboxSelectMultiple
        }
