from VIFAC.donors.Forms.donors import DonorForm
from VIFAC.donors.Forms.donations import DonationForm
from django.shortcuts import render
from django.template import loader


def index(request):
    context = {}
    return render(request, 'donors/donadores.html', context)


def new_donor(request):
    if request.method == "POST":
        # Get the posted form
        new_donor_form = DonorForm(request.POST)
        
        if new_donor_form.is_valid():
            full_name = new_donor_form.cleaned_data['full_name']
            integration_date = new_donor_form.cleaned_data['integration_date']
            state = new_donor_form.cleaned_data['state']
            
            
    else:
        new_donor_form = DonorForm()
    
    return render(request, 'new_donor.html', {})

def new_donation(request):
    if request.method == "POST":
        new_donation_form = DonationForm(request.POST)
        if new_donation_form.is_valid():
            description =  new_donation_form.cleaned_data['description']
            category = new_donation_form.cleaned_data['category']
            donor = new_donation_form.cleaned_data['donor']
        else:
            new_donation_form = DonationForm()
    
    return render(request, 'new_donation.html', {})