from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
import time

from .models import Listing, Report
# Create your tests here.

class ListingModelTests(TestCase):
	def test_listing_creation(self):
		listing = Listing.objects.create(
			name = "ABC Heights",
			address = "15, ABC Heights, Bond Street",
			town = "Ikeja",
			state = "lagos",
			fund_status = "pre-fund",
			shares_available = "1000000",
			investment_case = "great buy, go for it!",
			listing_details = "3 bedroom, furnished, 19 minutes from train station",
			unit_block = "30 units",
			floor_plan ="pic_folder/None/no-img.jpg"
		)
		time.sleep(0.1) # delays for 0.1 seconds
		now = timezone.now()
		self.assertLess(listing.created_at, now)

class ReportModelTests(TestCase):
	def setUp(self):
		self.listing = Listing.objects.create(
			name = "ABC Heights",
			address = "15, ABC Heights, Bond Street",
			town = "Ikeja",
			state = "lagos",
			fund_status = "pre-fund",
			shares_available = "1000000",
			investment_case = "great buy, go for it!",
			listing_details = "3 bedroom, furnished, 19 minutes from train station",
			unit_block = "30 units",
			floor_plan ="pic_folder/None/no-img.jpg"
		)


	def test_report_creation(self):
		report = Report.objects.create(
			title = "Residential report for Ikeja Property",
			overview = "Property is in good condition",
			report_type = "Solicitor's Report",
			listing = self.listing
		)

		self.assertIn(report, self.listing.report_set.all())

class ListingViewsTests(TestCase):
	def setUp(self):
		self.listing = Listing.objects.create(
			name = "ABC Heights",
			address = "15, ABC Heights, Bond Street",
			town = "Ikeja",
			state = "lagos",
			fund_status = "pre-fund",
			shares_available = "1000000",
			investment_case = "great buy, go for it!",
			listing_details = "3 bedroom, furnished, 19 minutes from train station",
			unit_block = "30 units",
			floor_plan ="pic_folder/None/no-img.jpg"
		)
		self.listing2 = Listing.objects.create(
			name = "ABC Heights",
			address = "15, ABC Heights, Bond Street",
			town = "Ikeja",
			state = "lagos",
			fund_status = "pre-fund",
			shares_available = "1000000",
			investment_case = "great buy, go for it!",
			listing_details = "3 bedroom, furnished, 19 minutes from train station",
			unit_block = "30 units",
			floor_plan ="pic_folder/None/no-img.jpg"
		)
		self.report = Report.objects.create(
			title = "Residential report for Ikeja Property",
			overview = "Property is in good condition",
			report_type = "Surveyor's Report",
			listing = self.listing
		)

	def test_listing_list_view(self):
		resp = self.client.get(reverse('listings:list'))
		self.assertEqual(resp.status_code, 200)
		self.assertIn(str(self.listing), str(resp.content))
		self.assertIn(str(self.listing2), str(resp.content))
		self.assertTemplateUsed(resp, 'listings/listing_list.html'),
		self.assertContains(resp, self.listing.name)

	def test_listing_detail_view(self):
		resp = self.client.get(reverse('listings:detail',
										kwargs={'pk': self.listing.pk}))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(self.listing, resp.context['listing'])
		self.assertTemplateUsed(resp, 'listings/listing_detail.html')
		
	def test_report_detail_view(self):
		resp = self.client.get(reverse('listings:report', 
									kwargs={'listing_pk': self.listing.pk,
									'report_pk': self.report.pk}))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(self.report, resp.context['report'])
		self.assertTemplateUsed(resp, 'listings/report_detail.html')
		