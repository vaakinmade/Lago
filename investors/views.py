from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, FormView
from .mixins import PageTitleMixin
from .models import RentAccount, Wallet
from listings.models import Listing
from django.contrib.auth import mixins, models, authenticate
from investors.forms import FundForm, PasswordChangeForm
from django import forms


class DashboardView(PageTitleMixin, mixins.LoginRequiredMixin, TemplateView):
	template_name = "investors/home.html"
	page_title = "investors area"
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)

		listing_query = Listing.objects.prefetch_related('investment_set','valuation_set')

		for val in listing_query:
			for investment in val.investment_set.all():
				if investment.investor_id == self.request.user.pk:
					if "pre-fund" in val.fund_status or "funding" in val.fund_status:
						context['pre_or_funding'] = True
					if "funded" in val.fund_status:
						context['funded'] = True

		context['dashboard'] = listing_query

		context['wallet'] = DashboardLayout.get_wallet_balance(self.request.user.id)
		return context


class DashboardLayout():
	@staticmethod
	def get_wallet_balance(investor_pk):
		#sess = SessionStore()
		try:
			return Wallet.objects.filter(investor_id=investor_pk).order_by('-created_at')[:1].get()
		except Wallet.DoesNotExist:
			obj = Wallet(
				investor_id=investor_pk,
				amount=0,
				balance=0,
				activity="Fund your wallet and start investing",
				transaction=Wallet.CREDIT)
			obj.save()
			return obj


class WalletListView(PageTitleMixin, mixins.LoginRequiredMixin, ListView):
	context_object_name = "statements"
	model = Wallet
	page_title = "Wallet History"
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(WalletListView, self).get_context_data(**kwargs)
		context['wallet'] = DashboardLayout.get_wallet_balance(self.request.user.id)
		return context

	def get_queryset(self):
		return Wallet.objects.filter(investor_id=self.request.user).order_by('-created_at')


class WalletCreateView(PageTitleMixin, mixins.LoginRequiredMixin, CreateView):
	form_class = FundForm
	template_name = 'investors/wallet_form.html'
	success_url = '/dashboard/fund-wallet'
	page_title = "Fund Wallet"
	transaction = "CR"

	def form_valid(self, form):
		if self.transaction == "CR":
			form.instance.investor = self.request.user
			form.instance.transaction = Wallet.CREDIT

			obj = DashboardLayout()
			wallet = obj.get_wallet_balance(self.request.user.id)
			form.instance.balance =  wallet.balance + form.cleaned_data['amount']

			return super(WalletCreateView, self).form_valid(form)

		elif self.transaction =="DR":
			form.instance.investor = self.request.user
			form.instance.transaction = Wallet.DEBIT
			wallet = self.get_balance(self.request.user.id)

			if wallet.balance >= form.cleaned_data['amount']:
				form.instance.balance =  wallet.balance - form.cleaned_data['amount']
			else:
				print("You do not have enough in your account")
				return HttpResponseRedirect(reverse('investors:withdraw'))
			return super(WalletCreateView, self).form_valid(form)

	def set_transaction_type(self, transaction_type):
		WalletCreateView.transaction = transaction_type
		return WalletCreateView.transaction

	def get_context_data(self, **kwargs):
		context = super(WalletCreateView, self).get_context_data(**kwargs)
		context['wallet'] = DashboardLayout.get_wallet_balance(self.request.user.id)
		return context


class WalletDebitView(WalletCreateView):
	success_url = '/dashboard/make-withdrawal'
	page_title = "Make Withdrawal"
	
	def form_valid(self, form):
		obj = WalletCreateView()
		obj.set_transaction_type(Wallet.DEBIT)
		return super(WalletDebitView, self).form_valid(form)


class RentAccountCreateView(PageTitleMixin, mixins.LoginRequiredMixin, CreateView):
	fields = ('account_name', 'account_number', 'sort_code')    
	model = RentAccount
	page_title = "Your Personal Bank Account Details"

	def form_valid(self, form):
		form.instance.investor = self.request.user
		return super(RentAccountCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(RentAccountCreateView, self).get_context_data(**kwargs)
		context['wallet'] = DashboardLayout.get_wallet_balance(self.request.user.id)
		return context


class PasswordChangeView(PageTitleMixin, mixins.LoginRequiredMixin, FormView):
	template_name = 'investors/security.html'
	form_class = PasswordChangeForm
	success_url = '/dashboard/change-password'
	page_title = 'Reset Password'


	def get_context_data(self, **kwargs):
		context = super(PasswordChangeView, self).get_context_data(**kwargs)
		context['wallet'] = DashboardLayout.get_wallet_balance(self.request.user.id)

		return context

	def get_form_kwargs(self):
		kwargs = super(PasswordChangeView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	# def form_valid(self, form):
	# 	# user = authenticate(username=self.request.user.username, password=form.cleaned_data['password'])
	# 	# if user is not None:
	# 	# 	user.set_password(form.cleaned_data['new_password'])
	# 	# 	user.save()
	# 	# 	return super(PasswordUpdateView, self).form_valid(form)
	# 	# else:
	# 	# 	password = form.cleaned_data['password']
	# 	# 	msg = "Incorrect Password"
	# 	# 	PasswordForm.add_error('password', msg)
		
	# 	return super(PasswordUpdateView, self).form_valid(form)
