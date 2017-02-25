# -*- coding: utf-8 -*-
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        default='',
        verbose_name='Contact Name',
        help_text="Contact's name"
    )

    first_lastname = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="Contact First Last Name",
        help_text="Contact's First Last Name"
    )

    second_lastname = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        default='',
        verbose_name="Contact First Last Name",
        help_text="Contact's First Last Name"
    )
    
    email = models.EmailField(
        max_length=256,
        null=False,
        blank=True,
        help_text='Contact\'s Email'
    )

    birthdate = models.DateField(
        null=False,
        blank=True
    )
    
    anniversary = models.DateField(
        null=False,
        blank=True,
    )

    phone_number = PhoneNumberField()
    
    

