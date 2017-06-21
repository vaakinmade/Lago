from django.contrib import admin
from .models import RentAccount, Wallet, BankTransfer


admin.site.register(RentAccount)
admin.site.register(Wallet)
admin.site.register(BankTransfer)
