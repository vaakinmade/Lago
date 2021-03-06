from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Listing(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	address = models.TextField()
	town = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	fund_status = models.CharField(max_length=225)
	shares_available = models.IntegerField(default=1000000)
	investment_case = models.TextField(blank=True, default='')
	listing_details = models.TextField(blank=True, default='')
	unit_block = models.CharField(max_length=225, default='')
	floor_plan = models.ImageField(upload_to='images/lagopoly', default='pic_folder/None/no-img.jpg')
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
   	    return reverse('listings:detail', kwargs={'pk': self.pk})


class ListingImage(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	listing = models.ForeignKey(Listing)
	slide_image = models.ImageField(upload_to='images/lagopoly', default='pic_folder/None/no-img.jpg')

	ORDER = []
	for i in range(1,7):
		values = i, i
		ORDER.append(values)
	
	ordering = models.IntegerField(
        choices=ORDER,
        default=0,
    )

	def __str__(self):
		return str(self.listing) + " 's Image"


class DocFile(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=225)
	overview = models.TextField()
	report_type = models.CharField(max_length=225)
	listing = models.ForeignKey(Listing, null=True)
	doc = models.FileField(upload_to='documents', max_length=225, default="documents/no-file.pdf")

	def __str__(self):
		if str(self.listing) is not None:
			return str(self.listing) + " 's Doc"
		return "General Investment Doc"


class Investment(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	listing = models.ForeignKey(Listing)
	investor = models.ForeignKey(User)
	unit_shares = models.IntegerField()
	unit_price = models.DecimalField(max_digits=5, decimal_places=5)
	investment_cost = models.DecimalField(max_digits=19, decimal_places=10)
	status = models.CharField(max_length=25, default='active')
	transaction_cost = models.DecimalField(max_digits=19, decimal_places=10)
	total_cost = models.DecimalField(max_digits=19, decimal_places=10)


	def get_absolute_url(self):
		return reverse('listings:invest', kwargs={
		        'listing_pk': self.listing_id
		    })

	def __str__(self):
		return "Investment by " + str(self.investor) + " on " + str(self.listing)

class Valuation(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	listing = models.ForeignKey(Listing)
	surveyor = models.CharField(max_length=225)
	solicitor = models.CharField(max_length=225)
	listing_value = models.IntegerField(default=0)
	capital_growth = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	rental_income = models.IntegerField(default=0)
	status = models.CharField(max_length=25, default='current')
	valuation_brief = models.TextField()

	def __str__(self):
		return self.listing.name + " Valuation"

class Financial(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	listing = models.ForeignKey(Listing)
	letting_management = models.DecimalField(max_digits=10, decimal_places=2)
	insurance = models.DecimalField(max_digits=10, decimal_places=2)
	maintenance = models.DecimalField(max_digits=10, decimal_places=2)
	corporation_tax = models.DecimalField(max_digits=10, decimal_places=2)
	void_allowance = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.listing.name + " Financial"


