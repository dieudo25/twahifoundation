from django.contrib.auth.forms import UserCreationForm

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
