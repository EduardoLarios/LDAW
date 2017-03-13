from .Forms.donors import DonorForm
from .Forms.donations import DonationForm
from django.shortcuts import render
from django.template import loader
import datetime
from .models.donors import Donor
from .models.donations import Donation
from .Forms.categories import CategoriesForm
from .models.categories import Category

def index(request):
    context = {}
    return render(request, 'donors/new_donor.html', context)


def placeholder(request):
    return None

def new_donor(request):
    today = datetime.datetime.now()
    
    if request.method == "POST":
        # Get the form through POST
        new_donor_form = DonorForm(request.POST)
        
        # Validate form data
        if new_donor_form.is_valid():
            
            # Get form variables
            full_name = new_donor_form.cleaned_data['full_name']
            integration_date = new_donor_form.cleaned_data['integration_date']
            state = new_donor_form.cleaned_data['state']
            city = new_donor_form.cleaned_data['city']
            street = new_donor_form.cleaned_data['street']
            number = new_donor_form.cleaned_data['number']
            reference = new_donor_form.cleaned_data['reference']
            contact_name = new_donor_form.cleaned_data['contact_name']
            contact_email = new_donor_form.cleaned_data['contact_email']
            contact_phone_number = new_donor_form.cleaned_data['contact_phone_number']
            contact_birthday = new_donor_form.cleaned_data['contact_birthday']
            contact_anniversary = new_donor_form.cleaned_data['contact_anniversary']
            
            context = {
                'full_name': full_name,
                'city': city,
                'today': today
            }
            
            # Create donor object
            donor = Donor.create(
                full_name = full_name,
                integration_date = integration_date,
                state = state,
                city = city,
                street = street,
                number = number,
                reference = reference,
                contact_name = contact_name,
                contact_email = contact_email,
                contact_phone_number = contact_phone_number,
                contact_birthday = contact_birthday,
                contact_anniversary = contact_anniversary
            )
            
            # Add donor to DB
            donor.save()
            
    else:
        new_donor_form = DonorForm()
    
    return render(request, 'donor_created.html', context)

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