# -*- coding: utf-8 -*-
from django.db import models

class Donation(models.Model):
	description = models.CharField(
		max_length = 1024,
		null = False,
		blank = False,
		default = '',
	)
	
	date = models.DateField(
		auto_now = True,
		null = False
	)
	
	code = models.CharField(
		null = False,
		blank = False,
		max_length = 8,
		verbose_name = _('code reference')
	)
	
	def __str__(self) -> str:
		return self.description
	
	class Meta(object):
		verbose_name = 'donor'
		verbose_name_plural = 'donors'
