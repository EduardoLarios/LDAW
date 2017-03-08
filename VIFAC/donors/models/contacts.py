# -*- coding: utf-8 -*-
from django.db import models
from datetime import *
from phonenumber_field.modelfields import PhoneNumberField

__all__ = [ 'Contact' ]

class Contact(models.Model):
    full_name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        default='',
        db_index=True,
        verbose_name=('Contact Name'),
        help_text=("Contact's name")
    )
    phone = PhoneNumberField(
        blank=False,
        null=False,
    )
    email = models.EmailField()
    birthday = models.DateField(
        blank=True,
        null=False,
        verbose_name=('Birthday'),
        help_text=('Birthday of donor'),
    )
    aniversary = models.DateField(
        blank=True,
        null=False,
        verbose_name=('Aniversary'),
        help_text=('Aniversary of the donor'),
    )
