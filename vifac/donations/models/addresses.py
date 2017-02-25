# -*- coding: utf-8 -*-
from django.db import models

class Address(models.Model):
	street = models.CharField(
		max_length = 256,
		null = False,
		blank = False,
		default = ''
	)
