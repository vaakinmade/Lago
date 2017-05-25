from django.conf.urls import url

from . import views

urlpatterns = [
	#url(r'^$', views.listing_list, name='list'),
	url(r'(?P<listing_pk>\d+)/(?P<report_pk>\d+)/$', views.report_detail,
		name='report'),
	url(r'pre-invest/(?P<listing_pk>\d+)/$', views.prep_investment, name='invest'),
	url(r'(?P<pk>\d+)/$', views.ListingDetailView.as_view(), name='detail'),
	url(r'^$', views.ListingListView.as_view(), name='list'),
	url(r'^create/$', views.ListingCreateView.as_view(), name='create'),
	url(r'^edit/(?P<pk>\d+)/$', views.ListingUpdateView.as_view(), name='update'),
]