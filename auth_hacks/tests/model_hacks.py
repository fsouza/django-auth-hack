# -*- coding: utf-8 -*-
import unittest

from django import forms
from django.db import models as django_models

from auth_hacks import models


class SampleModel(django_models.Model):
    name = django_models.CharField(max_length=30)

    class Meta:
        app_label = 'auth_hacks'


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel


class AuthHackModelTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        models.hack_model(SampleModel, "name")

    def test_deve_mudar_max_length_do_field_para_100(self):
        self.assertEquals(100, SampleModel._meta.get_field("name").max_length)

    def test_deve_mudar_validators_do_field(self):
        validator = SampleModel._meta.get_field("name").validators[0]
        self.assertEquals(100, validator.limit_value)


class AuthHackFormTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        models.hack_form(SampleModelForm, "name")
        cls.field = SampleModelForm.base_fields["name"]

    def test_deve_mudar_max_length_de_field_no_formulario(self):
        self.assertEquals(100, self.field.max_length)

    def test_deve_mudar_attr_max_length_do_widget_do_formulario(self):
        self.assertEquals(100, self.field.widget.attrs['maxlength'])

    def test_deve_mudar_help_text_para_exibir_descricao_correta(self):
        self.assertEquals(u"Obrigatório. 100 caracteres ou menos. Somente letras, dígitos e @/./+/-/_.", self.field.help_text)

    def test_deve_mudar_validator_do_field(self):
        validator = self.field.validators[0]
        self.assertEquals(100, validator.limit_value)
