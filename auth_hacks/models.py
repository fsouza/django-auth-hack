# -*- coding: utf-8 -*-
import sys

from django.conf import settings
from django.core import validators


MAX_LENGTH = getattr(settings, 'USERNAME_MAX_LENGTH', 100)


def hack_validators(field):
    for i, v in enumerate(field.validators):
        if isinstance(v, validators.MaxLengthValidator):
            field.validators.pop(i)

    field.validators.insert(0, validators.MaxLengthValidator(MAX_LENGTH))


def hack_model(model_class, field_name):
    field = model_class._meta.get_field(field_name)
    field.max_length = MAX_LENGTH
    hack_validators(field)


def hack_form(form_class, field_name):
    if hasattr(form_class, 'declared_fields') and form_class.declared_fields:
        fields = form_class.declared_fields
    elif hasattr(form_class, 'base_fields') and form_class.base_fields:
        fields = form_class.base_fields
    else:
        raise TypeError('Provided object: %s doesnt seem to be a valid Form or '
                        'ModelForm class.' % form_class)
    username = fields[field_name]
    username.help_text = "Obrigatório. %s caracteres ou menos. Somente letras, dígitos e @/./+/-/_." % MAX_LENGTH
    hack_validators(username)
    username.max_length = MAX_LENGTH
    username.widget.attrs['maxlength'] = MAX_LENGTH


def hack_forms():
    forms = [
        "django.contrib.auth.forms.UserCreationForm",
        "django.contrib.auth.forms.UserChangeForm",
        "django.contrib.auth.forms.AuthenticationForm",
    ]

    for f in forms:
        module_name, sep, class_name = f.rpartition(".")
        if not module_name in sys.modules:
            __import__(module_name)
        module = sys.modules[module_name]
        cls = getattr(module, class_name)
        hack_form(cls, "username")


from django.contrib.auth import models
hack_model(models.User, "username")
hack_forms()
