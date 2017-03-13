# -*- coding: utf-8 -*-
from .categories import Category
from .donors import Donor
from django.db import models

#TODO Check model here
class Donation(models.Model):
    donor = models.ForeignKey(
        Donor,
    )
    
    description = models.CharField(
        max_length = 1024,
        default = '',
        help_text = 'a small description of the donation'
    )
    
    category = models.OneToOneField(Category,
        verbose_name = 'Category',
        help_text = 'How one would classify the donation: money, food, etc.'
    )

    date = models.DateField(
        auto_now = True,
    )
    
    
    def __str__(self) -> str:
        return self.code + ' - ' + self.description
    
    class Meta(object):
        verbose_name = 'donation'
        verbose_name_plural = 'donations'
