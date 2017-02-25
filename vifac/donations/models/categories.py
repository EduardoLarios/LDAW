# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name = "Category name",
        help_text = "Category's name"
    )

    description = models.CharField(
        max_length = 256,
        null = False,
        blank = False,
        default = '',
        verbose_name = "Description",
        help_text = "Description's name"
    )
