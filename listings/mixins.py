from .models import Investment, Listing
from django.core.exceptions import ObjectDoesNotExist


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

    def update_listing_shares(self, listing_pk, unit_shares):
        listing = Listing.objects.get(id=listing_pk)
        listing.shares_available -= unit_shares
        return listing

    #investment.unit_shares = 