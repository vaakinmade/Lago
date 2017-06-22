from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),

]