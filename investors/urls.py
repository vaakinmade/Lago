from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^payment-account/$', views.RentAccountCreateView.as_view(), name='account'),
    url(r'^$', views.DashboardView.as_view(), name='home'),
    url(r'^wallet/$', views.WalletListView.as_view(), name='statement'),
    url(r'^fund-wallet/$', views.WalletCreateView.as_view(), name='fund'),
    url(r'^make-withdrawal/$', views.WalletDebitView.as_view(), name='withdraw'),
]