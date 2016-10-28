from django.test import TestCase
from django.shortcuts import resolve_url as r

from listimoveis.login.forms import LoginForm


class LoginTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('login:login'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'login/login.html')

    def test_form_has_fields(self):
        form = LoginForm()
        expected = ['username', 'password']
        self.assertSequenceEqual(expected, list(form.fields))