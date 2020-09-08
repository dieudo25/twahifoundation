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

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = ''
