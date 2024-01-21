from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def all_logins(request):
    return render(request, 'all_logins.html' )

def donor_login(request):
    if request.method == "POST":
        email = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        user = authenticate(username=email,password=pwd)
        if user:
            login(request, user)
            error = 'no'

        else:
            error = 'yes'
    return render(request, 'donor_login.html', locals())
    
def distributor_login(request):
    return render(request, 'distributor_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def donor_reg(request):
    error = ""

    if request.method == "POST":
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        em = request.POST.get('email')
        contact = request.POST.get('contact')
        pwd = request.POST.get('pwd')
        userpc = request.FILES.get('userpic')
        address = request.POST.get('address')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            Donor.objects.create(user=user, contact=contact, userpic=userpc, address=address)

            error = 'no'
        except:
            error = 'yes'
    return render(request, 'donor_reg.html', locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donor_home.html')

def donor_base(request):
    return render(request, 'donor_base.html')


def Logout(request):
    logout(request)
    return redirect('index')
    
def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method == "POST":
       donationname = request.POST.get('donation') 
       donationpic = request.FILES.get('donationpic') 
       location = request.POST.get('collectionlocation') 
       descroption = request.POST.get('description') 

       try:
           Donation.objects.create(donor=donor, donationname=donationname,donationpic = donationpic, collectionlocation=location, descroption= descroption, status = "pending")
           error = "no"
       except:
           error = "yes"
    return render(request, 'donate_now.html', locals())

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request, 'donation_history.html')