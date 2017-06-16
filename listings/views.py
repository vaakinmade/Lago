from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView 
from .models import Listing, Report, Valuation, Investment, ListingImage
from django.contrib import messages
from .mixins import PageTitleMixin, InvestmentOperations
from django.contrib.auth.decorators import login_required
from .forms import InvestmentForm, ListingImageForm
from . import models
from django.db.models import Prefetch
from django.contrib import messages
from blogs.mixins import ImageOperations


class ListingListView(ListView):
    context_object_name = "listings"
    model = models.Listing

    def get_queryset(self):
        return  Listing.objects.exclude(id=1).order_by('-created_at').prefetch_related(
            Prefetch('investment_set',
                queryset=Investment.objects.filter(status='active'),
                to_attr='active_investments'),
            Prefetch('valuation_set',
                queryset=Valuation.objects.filter(status='current'),
                to_attr='active_valuations')
                )


class ListingDetailView(DetailView):
    model = models.Listing

    def get_queryset(self):
        return  Listing.objects.filter(id=self.kwargs['pk']).prefetch_related(
            Prefetch('investment_set',
                queryset=Investment.objects.filter(status='active'),
                to_attr='active_investments'),
            Prefetch('valuation_set',
                queryset=Valuation.objects.filter(status='current'),
                to_attr='active_valuations'),
            Prefetch('listingimage_set',
                queryset=ListingImage.objects.filter(listing_id=self.kwargs['pk']).order_by('ordering'),
                to_attr='ordered_images')
                )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        listing_images = ListingImage.objects.filter(listing_id=self.kwargs['pk'])
        obj_image = ImageOperations()
        for image in listing_images:
            obj_image.process_ratio(image.slide_image)

        return context





class ListingCreateView(PageTitleMixin, LoginRequiredMixin, CreateView):
    success_url = '/create'
    template_name = 'listings/listing_form.html'
    page_title = 'Add a new Listing'
    model = models.Listing
    fields = ('name', 'address', 'town', 'state', 'fund_status', 'shares_available',
             'investment_case', 'listing_details', 'unit_block','floor_plan')

    def get_initial(self):
        initial = super().get_initial()
        initial['coach'] = self.request.user.pk
        return initial


class ListingImageView(PageTitleMixin, LoginRequiredMixin, FormView):
    form_class =ListingImageForm
    page_title = 'Listing Images'
    template_name = 'listings/listing_form.html'

    def form_valid(self, form):
        images = self.request.FILES.getlist('slide_images')
        listing = Listing.objects.get(id=self.kwargs['listing_pk'])
        for image in images:
            ListingImage.objects.create(listing_id=listing.id, slide_image=image)
        
        messages.add_message(self.request, messages.SUCCESS, "All {} Images uploaded.".format(len(images)))    
        return super(ListingImageView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listings:add_images', kwargs={'listing_pk': self.kwargs['listing_pk']})


class ListingUpdateView(PageTitleMixin, LoginRequiredMixin, UpdateView):
    fields = ('name', 'address', 'town', 'state', 'fund_status', 'shares_available',
             'investment_case', 'listing_details', 'unit_block','floor_plan')
    model = models.Listing

    def get_page_title(self):
        obj = self.get_object()
        return 'Update {}'.format(obj.name)

    def get_success_url(self):
        return reverse('listings:update', kwargs={'pk': self.kwargs['pk']})


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
            success_message = "Well done! You have committed funds to invest in a property."

            obj = InvestmentOperations()
            if obj.check_available_shares(valuation.listing.id, form.cleaned_data['unit_shares']) is False:
                messages.add_message(request, messages.INFO,
                             "Error: Unfortunately, there aren't that many shares left for this property.")
                return HttpResponseRedirect(investment.get_absolute_url())

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