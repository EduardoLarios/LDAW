from donors.models import Category, Address, Donation, Contact
from django.db import models
from datetime import *
from phonenumber_field.modelfields import PhoneNumberField

__all__ = [ 'Donors' ]


class Donor(models.Model):

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

    country = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = 'México',
        verbose_name= "Country"
    )
    
    estate = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name= "Estate"
    )

    city = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name= "City"
    )
    
    street = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name= "Street"
    )
    
    number = models.CharField(
        max_length = 12,
        null = False,
        blank = False,
        default = '',
        verbose_name= "Number"
    )
    
    reference =  models.CharField(
        max_length = 256,
        null = False,
        blank = True,
        default = '',
        verbose_name = "Reference",
        help_text = "Whoever introduced the donor to Vifac"
    )

    contact_name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        default='',
        verbose_name='Contact Name',
        help_text="Contact's name"
    )

    contact_first_lastname = models.CharField(
        max_length=256,
        null=False,
        blank=True,
        default='',
        verbose_name="Contact First Last Name",
        help_text="Contact's First Last Name"
    )

    contact_second_lastname = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        default='',
        verbose_name="Contact First Last Name",
        help_text="Contact's First Last Name"
    )

    contact_email = models.EmailField(
        max_length=256,
        null=False,
        blank=True,
        help_text="Contact's Email"
    )

    contact_birthdate = models.DateField(
        null=False,
        blank=True
    )

    contact_anniversary = models.DateField(
        null=False,
        blank=True
    )

    contact_phone_number = PhoneNumberField()

    def __str__(self) -> str:
        return self.full_name

    class Meta(object):
        verbose_name = 'donor'
        verbose_name_plural = 'donors'