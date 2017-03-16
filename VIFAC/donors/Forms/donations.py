# -*- coding: utf-8 -*-
from ..models.categories import Category
from ..models.donors import Donor
from django import forms


class DonationForm(forms.Form):
	
	description = forms.CharField(
		max_length = 512,
		label = "Descripción de la donación",
		help_text = 'Arroz, 500 pesos, etc...'
	)
	
	category = forms.ChoiceField(
		choices = Category,
		label = 'Categoría'
	)
	
	donor = forms.ChoiceField(
		choices = Donor,
		label = 'Donador'
	)
