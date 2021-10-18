from django.contrib import admin
from warung.models import BioToko, Category, Stocker, good
from deposit.models import Deposit

admin.site.register(BioToko)
admin.site.register(Category)
admin.site.register(Stocker)
admin.site.register(good)
admin.site.register(Deposit)
# Register your models here.
