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
        default=''
    )
    email = models.EmailField(
        null=False,
        default=''
    )
    aniversary = models.DateField(
        null=False,
        default=date.today()

    )
    birthdate = models.DateTimeField(blank=True, null=True)

