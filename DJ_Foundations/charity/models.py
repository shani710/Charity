from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null= True)
    address = models.CharField(max_length=300, null = True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Distributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null= True)
    address = models.CharField(max_length=300, null = True)
    userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme = models.CharField(max_length = 300, null=True)
    status = models.CharField(max_length=20, null= True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremarks = models.CharField(max_length=200, null= True)
    updationdate = models.DateField(null= True)
 
    def __str__(self):
        return self.user.username



class DonationArea(models.Model):
    location = models.CharField(max_length=100, null= True)
    discription = models.CharField(max_length=300, null = True)
    creationdate = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.areaname 
    
class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100, null= True)
    donationpic = models.FileField(null=True)
    collectionlocation = models.CharField(max_length=300, null = True)
    description = models.CharField(max_length=300, null = True)
    status = models.CharField(max_length=50, null= True)
    donationdate = models.DateField(auto_now_add=True)
    adminremarks = models.CharField(max_length=200, null= True)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    donationarea = models.ForeignKey(DonationArea, on_delete=models.CASCADE)
    distributorremarks = models.CharField(max_length=200, null= True)
    updationdate = models.DateField(null=True)
 
    def __str__(self):
        return self.id
    
class Gallery(models.Model):
    donotion = models.ForeignKey(Donation, on_delete=models.CASCADE)
    delivarynpic = models.FileField(null=True)
    creationdate = models.DateField(auto_now_add=True)

    
 
    def __str__(self):
        return self.id