from django.shortcuts import get_object_or_404, render
#from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Listing, Report
# Create your views here.

#class FundProperty(LoginRequiredMixin):

#class SharesTrader(LoginRequiredMixin):

#class SharesManager(LoginRequiredMixin):

#class Dashboard(LoginRequiredMixin):

def listing_list(request):
	listings = Listing.objects.all
	return render(request, 'listings/listing_list.html', {'listings': listings})

def home(request):
	return render(request, 'home.html')

def listing_detail(request, pk):
	listing = get_object_or_404(Listing, pk=pk)
	return render(request, 'listings/listing_detail.html', {'listing': listing})

def report_detail(request, listing_pk, report_pk):
	report = get_object_or_404(Report, listing_id=listing_pk, pk=report_pk)
	return render(request, 'listings/report_detail.html', {'report': report})