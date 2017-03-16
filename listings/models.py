from django.db import models

# Create your models here.
class Listing(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=225)
	address = models.TextField()
	town = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	fund_status = models.CharField(max_length=225)
	current_valuation = models.IntegerField()
	shares_available = models.IntegerField(default=1000000)
	rental_income = models.DecimalField(max_digits=19, decimal_places=10)
	capital_growth = models.DecimalField(max_digits=5, decimal_places=2)
	investment_case = models.TextField(blank=True, default='')
	listing_details = models.TextField(blank=True, default='')
	unit_block = models.CharField(max_length=225, default='')


	#floor_plan = models.pathtoimagefile
	def __str__(self):
		return self.name

class Report(models.Model):
	title = models.CharField(max_length=225)
	overview = models.TextField()
	report_type = models.CharField(max_length=225)
	listing = models.ForeignKey(Listing)
	#pdf_path = models.FileField(upload_to=None, max_length=225)

	def __str__(self):
		return self.title