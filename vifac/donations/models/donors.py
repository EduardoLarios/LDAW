# -*- coding: utf-8 -*-
from vifac.donations.models import Category, Address, Donation, Contact
from django.db import models
from datetime import *

__all__ = [ 'Donors' ]

class Donors(models.Model):

    full_name = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        db_index = True,
        verbose_name = 'Donor Name',
        help_text = "Donor's name"
    )

    category = models.OneToOneField(Category,
        null = False,
        blank = False,
        verbose_name = 'Category'
    )

    donation = models.ForeignKey(Donation,
        null = False,
        blank = True,
        verbose_name = 'Donation',
        help_text = "Whatever the donation may be"
    )

    integration_date = models.DateField(
        null = False,
        blank = False,
        default = date.today(),
        verbose_name = 'Integration Date',
        help_text = "Date when the donor is integrated into Vifac"
    )

    address = models.OneToOneField(Address,
        null = False,
        blank = False,
        verbose_name = 'Address',
        help_text = "Donor's address"
    )

    reference = models.CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = "Reference",
        help_text = "Whoever introduced the donor to Vifac"
    )

    contacts = models.ForeignKey(Contact,
        null = False,
        blank = False,
        verbose_name = 'Contact Information',
        help_text = 'Contact information for the donor'
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta(object):
        verbose_name = 'donor'
        verbose_name_plural = 'donors'
