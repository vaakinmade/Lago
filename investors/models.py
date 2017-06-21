from django.db import models
from django.contrib.auth.models import User


class RentAccount(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	account_name = models.CharField(max_length=50)
	account_number = models.IntegerField()
	sort_code = models.IntegerField()
	investor = models.ForeignKey(User)


class BankTransfer(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	reference_code = models.CharField(max_length=50)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	status = models.TextField()
	investor = models.ForeignKey(User)


class Wallet(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	balance = models.DecimalField(max_digits=10, decimal_places=2)
	activity = models.TextField()
	investor = models.ForeignKey(User)

	CREDIT = 'CR'
	DEBIT = 'DR'
	TRANSACTION = (
	    (CREDIT, 'Credit'),
	    (DEBIT, 'Debit'),
	)
	transaction = models.CharField(
        max_length=2,
        choices=TRANSACTION,
        default='',
    )

	def __str__(self):
		return self.investor.username + "'s Wallet"