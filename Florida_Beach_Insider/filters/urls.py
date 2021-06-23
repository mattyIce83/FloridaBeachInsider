from django.conf.urls import url

from . import views

urlpatterns = (
    # urls for Filter
    url(r'^filters/filter/$', views.FilterListView.as_view(), name='filters_filter_list'),
    url(r'^filters/filter/create/$', views.FilterCreateView.as_view(), name='filters_filter_create'),
    url(r'^filters/filter/detail/(?P<pk>\S+)/$', views.FilterDetailView.as_view(), name='filters_filter_detail'),
    url(r'^filters/filter/update/(?P<pk>\S+)/$', views.FilterUpdateView.as_view(), name='filters_filter_update'),
)

