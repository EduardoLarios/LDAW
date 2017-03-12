# -*- coding: utf-8 -*-
from VIFAC.donors.models import Category
from django.db import models


class Donation(models.Model):
    code = models.CharField(
        max_length = 8,
        verbose_name ='code reference'
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
