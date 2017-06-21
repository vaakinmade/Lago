from .models import Investment, Listing, Valuation
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch


class PageTitleMixin:
    page_title = ''

    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.get_page_title()
        return context


class InvestmentOperations:
    def get_investment(self, investor_pk, listing_pk):
        try:
            investment = Investment.objects.get(investor_id=investor_pk, listing_id=listing_pk, status='active')
            return investment
        except ObjectDoesNotExist:
            return "Investor owns no preexisting investment in property"

    def archive_update_investment(self, investor_pk, listing_pk):
        investment = self.get_investment(investor_pk, listing_pk)
        if not isinstance(investment, str):
            investment.status = "archived"
            investment.save()
            return investment.status, investment.unit_shares

        return investment

    def get_listing(self, listing_pk):
         return Listing.objects.get(id=listing_pk)

    def update_listing_shares(self, listing_pk, unit_shares):
        listing = self.get_listing(listing_pk)
        listing.shares_available -= unit_shares
        return listing

    def check_available_shares(self, listing_pk, requested_shares):
        listing = Listing.objects.filter(id=listing_pk).prefetch_related( 
            Prefetch('valuation_set',
                queryset=Valuation.objects.filter(status='current'),
                to_attr='current_valuation'
                ))
        print("shares available", listing[0].shares_available)
        if requested_shares > listing[0].shares_available:
            listing_valuation = listing[0].current_valuation[0].listing_value
            remaining_amount = listing[0].shares_available * (listing_valuation/1000000)
            return False, remaining_amount
        else:
            return True, None


    #investment.unit_shares = 