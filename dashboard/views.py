from django.shortcuts import render
from django.views.generic import TemplateView
from listings import models


class DashboardView(TemplateView):
	template_name = "dashboard/home.html"

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)

		listing_query = models.Listing.objects.prefetch_related('investment_set','valuation_set')

		for val in listing_query:
			for investment in val.investment_set.all():
				if investment.investor_id == self.request.user.pk:
					if "pre-fund" in val.fund_status or "funding" in val.fund_status:
						context['pre_or_funding'] = True
					if "funded" in val.fund_status:
						context['funded'] = True

		context['dashboard'] = listing_query
		return context