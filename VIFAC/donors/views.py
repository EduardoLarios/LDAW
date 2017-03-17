from .forms.categories import CategoriesForm
from .forms.donations import DonationForm
from .forms.donors import DonorForm

from .models.categories import Category
from .models.donations import Donation
from .models.donors import Donor

from django.shortcuts import render
import datetime
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    context = {}
    return render(request, 'donors/index.html', context)

def new_donor(request):

     context = { 'today': datetime.datetime.now() }

     if request.method == "POST":

         # Get the form through POST
         new_donor_form = DonorForm(request.POST)

         # Validate form data
         if new_donor_form.is_valid():

             # Get form variables
             # Create donor object
             context['donor'] = Donor.objects.create(**new_donor_form.cleaned_data)
             return render(request, 'donors/donor_created.html', context, status = 201)

         context['form'] = new_donor_form
         return render(request, 'donors/new_donor.html', context)

     else: new_donor_form = DonorForm()

     context['form'] = new_donor_form
     
     return render(request, 'donors/new_donor.html', context)


def new_donation(request):
    
    donors = Donor.objects.all().values('id', 'full_name')
    categories = Category.objects.all().values('id', 'name')
    context = {'today': datetime.datetime.now(), 'categories': categories, 'donors': donors}
    
    if request.method == "POST":
        
        # Get the form through POST
        new_donation_form = DonationForm(request.POST)
        
        # Validate form data
        if new_donation_form.is_valid():
            # Get form variables
            # Create donor object
            context['donation'] = Donation.objects.create(**new_donation_form.cleaned_data)
            return render(request, 'donors/donation_created.html', context, status = 201)
        
        context['form'] = new_donation_form
        return render(request, 'donors/new_donation.html', context)
    
    else:
        new_donation_form = DonationForm()
    
    context['form'] = new_donation_form
    
    return render(request, 'donors/new_donation.html', context)

        
