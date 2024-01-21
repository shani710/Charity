from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def all_logins(request):
    return render(request, 'all_logins.html' )

def donor_login(request):
    return render(request, 'donor_login.html')
    
def distributor_login(request):
    return render(request, 'distributor_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def donor_reg(request):
    return render(request, 'donor_reg.html')