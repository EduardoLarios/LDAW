from .Forms.categories import CategoriesForm
from .Forms.donations import DonationForm
from .models.categories import Category
from .models.donations import Donation
from django.shortcuts import render
from .Forms.donors import DonorForm
# from .models.donors import State
from django.template import loader
from .models.donors import Donor
import datetime
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'donors/index.html', context)

def creation_view(model, form_cls):
    
    name = model._meta.model_name
    
    def view(request):
    
        context = { 'today': datetime.datetime.now() }
    
        if request.method == "POST":
        
            # Get the form through POST
            form = form_cls(request.POST)
        
            # Validate form data
            if form.is_valid():
                # Get form variables
                # Create donor object
                context['donor'] = model.objects.create(**form.cleaned_data)
                return render(request, 'donors/%s_created.html' % name, context, status = 201)
        
            context['form'] = form
            return render(request, 'donors/new_%s.html' % name, context)
    
        else: form = DonorForm()
    
        context['form'] = form
        return render(request, 'donors/new_%s.html' % name, context)

    return view

new_donor = creation_view(Donor, DonorForm)

# def new_donor(request):
#
#     context = { 'today': datetime.datetime.now() }
#
#     if request.method == "POST":
#
#         # Get the form through POST
#         new_donor_form = DonorForm(request.POST)
#
#         # Validate form data
#         if new_donor_form.is_valid():
#
#             # Get form variables
#             # Create donor object
#             context['donor'] = Donor.objects.create(**new_donor_form.cleaned_data)
#             return render(request, 'donors/donor_created.html', context, status = 201)
#
#         context['form'] = new_donor_form
#         return render(request, 'donors/new_donor.html', context)
#
#     else: new_donor_form = DonorForm()
#
#     context['form'] = new_donor_form
#     return render(request, 'donors/new_donor.html', context)

def new_donation(request):
    if request.method == "POST":
        #Form through POST
        new_donation_form = DonationForm(request.POST)
        
        if new_donation_form.is_valid():
        
            #Variables
            description = new_donation_form.cleaned_data['description']
            category =  new_donation_form.cleaned_data['category']
            donor = new_donation_form.cleaned_data['donor']
            
            donation = Donation.create(
                description = description,
                category = category,
                donor = donor
            )
            
            donation.save()
            
    else:
        new_donation_form = DonationForm()
        
def new_category(request):
    if request.method == "POST":
        #Form through POST
        new_category_form = CategoriesForm(request.POST)
        
        if new_category_form.is_valid():
            
            name =  new_category_form.cleaned_data['name']
            description = new_category_form.cleaned_data['description']
            
            category = Category.create(
                name = name,
                description = description
            )
            
            category.save()
            
    else:
        new_category_form = CategoriesForm()
