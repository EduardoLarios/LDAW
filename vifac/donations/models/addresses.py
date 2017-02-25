# -*- coding: utf-8 -*-
from django.db import models
from cities_light.models import Region, City

class Address(models.Model):
	street = models.CharField(
		max_length = 256,
		null = False,
		blank = False,
		default = ''
	)
	
	number = models.CharField(
		max_length = 64,
		null = False,
		blank = False,
		default = ''
	)
	
	suburb = models.CharField(
		max_length = 256,
		null = False,
		blank = False,
		default = ''
	)
	
	postal_code = models.CharField(
		max_length = 16,
		null = False,
		blank = False,
		default = ''
	)
	
	str_format = models.CharField(
		max_length = 512,
		null = False,
		blank = False,
		verbose_name = _('formatting string')
	)
	
	city = models.OneToOneField(City)
	
	region = models.OneToOneField(Region)
	
	def __str__(self) -> str:
		data = {
			'city': self.city.name,
			'region': self.city.region.name,
			'street': self.street,
			'number': self.number,
			'suburb': self.suburb,
			'postal_code': self.postal_code,
		}
		
		return self.str_format.format(**data)
	
	class Meta(object):
		verbose_name = 'address'
		verbose_name_plural = 'addresses'
	
