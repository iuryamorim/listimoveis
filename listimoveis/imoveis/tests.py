from django.test import TestCase
from django.shortcuts import resolve_url as r

from listimoveis.imoveis.forms import ImoveisForm


class ImoveisTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('imoveis:imoveis'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'imoveis/imovel-form.html')

    def test_form_has_fields(self):
        form = ImoveisForm()
        expected = ['name', 'address', 'photo', 'description', 'cep', 'slug']
        self.assertSequenceEqual(expected, list(form.fields))