from django.test import TestCase

from account.forms.user import UserCreateForm


class TestForms(TestCase):
    "Test User forms"

    def test_user_create_form_valid_data(self):
        ""

        form = UserCreateForm(data={
            'username': 'user1',
            'firstname': 'Jonh',
            'lastname': 'Smith',
            'email': 'jonhSmith@test.com',
            'password1': 'test12d9',
            'password2': 'test12d9',
        })

        self.assertTrue(form.is_valid())

    def test_user_create_form_no_valid(self):
        ""

        form = UserCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
