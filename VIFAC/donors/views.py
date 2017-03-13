from VIFAC.donors.Forms.donors import DonorForm
from django.shortcuts import render
from django.template import loader
import datetime
from VIFAC.donors.models import Donor


'''def index(request):
    context = {}
    return render(request, 'donor`s/new_donor.html', context)
'''

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
