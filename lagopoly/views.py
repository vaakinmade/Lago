from django.shortcuts import render
from django.http import HttpResponse
from listings import models
from django.views.generic import View, TemplateView, ListView
from django.db.models import Prefetch


def home(request):
	return render(request, 'home.html')

def faqs(request):
	return render(request, 'faqs.html')

def privacy(request):
	return render(request, 'privacy.html')

def termsofuse(request):
	return render(request, 'termsofuse.html')


class HelloWorldView(View):
	def get(self, request):
		return HttpResponse("Hello World!")


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["listings"] = self.get_latest_listing
		return context

	def get_latest_listing(self, **kwargs):
		return  models.Listing.objects.order_by('-created_at')[:1].prefetch_related(
            Prefetch('investment_set',
                queryset=models.Investment.objects.filter(status='active'),
                to_attr='active_investments'),
            Prefetch('valuation_set',
                queryset=models.Valuation.objects.filter(status='current'),
                to_attr='active_valuations')
                )
