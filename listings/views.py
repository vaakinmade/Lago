from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView 
from .models import Listing, Report, Valuation, Investment
from django.contrib import messages

from .mixins import PageTitleMixin, InvestmentOperations
from django.contrib.auth.decorators import login_required
from .forms import InvestmentForm
from . import models


class ListingListView(ListView):
	context_object_name = "listings"
	model = models.Listing


class ListingDetailView(DetailView):
	model = models.Listing


class ListingCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
    fields = ('name', 'address', 'town', 'state', 
    			'fund_status', 'shares_available', 'investment_case', 'listing_details', 'unit_block')
    model = models.Listing
    page_title = 'Add a new Listing'

    def get_initial(self):
        initial = super().get_initial()
        initial['coach'] = self.request.user.pk
        return initial


class ListingUpdateView(PageTitleMixin, LoginRequiredMixin, UpdateView):
    fields = ('name', 'address', 'town', 'state', 
    			'fund_status', 'shares_available', 'investment_case', 'listing_details', 'unit_block')
    model = models.Listing

    def get_page_title(self):
        obj = self.get_object()
        return 'Update {}'.format(obj.name)


@login_required
def prep_investment(request, listing_pk):
    valuation = get_object_or_404(Valuation, listing_id=listing_pk, status='current')
    form = InvestmentForm()

    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid:
            investment = form.save(commit=False)
            investment.listing = valuation.listing
            investment.investor = request.user
            success_message = "You have successfully made an investment!"

            obj = InvestmentOperations()
            archive_result = obj.archive_update_investment(request.user.id, valuation.listing.id)
            listing_shares = obj.update_listing_shares(valuation.listing.id, form.cleaned_data['unit_shares'])

            if "archived" in archive_result:
                investment.unit_shares = form.cleaned_data['unit_shares']  + archive_result[-1]
                investment.save()
                listing_shares.save()
                messages.add_message(request, messages.SUCCESS,
                     success_message)
                return HttpResponseRedirect(investment.get_absolute_url())

            else:
                print ("Investor owns no preexisting investment in property")

                investment.save()
                listing_shares.save()
                messages.add_message(request, messages.SUCCESS,
                             success_message)
                return HttpResponseRedirect(investment.get_absolute_url())

    return render(request, 'listings/pre_investment.html', {'form': form, 'preinvestment': valuation})


def home(request):
	return render(request, 'home.html')


def report_detail(request, listing_pk, report_pk):
    report = get_object_or_404(Report, listing_id=listing_pk, pk=report_pk)
    return render(request, 'listings/report_detail.html', {'report': report})

#def listing_list(request):
#   listings = Listing.objects.all
#   return render(request, 'listings/listing_list.html', {'listings': listings})

#def listing_detail(request, pk):
#   listing = get_object_or_404(Listing, pk=pk)
#   return render(request, 'listings/listing_detail.html', {'listing': listing})