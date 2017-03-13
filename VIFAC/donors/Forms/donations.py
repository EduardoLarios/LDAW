# -*- coding: utf-8 -*-
from django import forms
from VIFAC.donors.models.donors import Donor
from VIFAC.donors.models.categories import Category


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
		choices=Donor,
		label = 'Donador'
	)