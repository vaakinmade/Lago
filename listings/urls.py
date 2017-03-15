from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.listing_list, name='list'),
	url(r'(?P<listing_pk>\d+)/(?P<report_pk>\d+)/$', views.report_detail,
		name='report'),
	url(r'(?P<pk>\d+)/$', views.listing_detail, name='detail'),   
]