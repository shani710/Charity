from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Donor)
admin.site.register(Distributor)
admin.site.register(Donation)
admin.site.register(DonationArea)
admin.site.register(Gallery)

