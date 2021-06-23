from django.conf.urls import url

from . import views

urlpatterns = (
    # urls for Author
    url(r'^authors/author/$', views.AuthorListView.as_view(), name='authors_author_list'),
    url(r'^authors/author/create/$', views.AuthorCreateView.as_view(), name='authors_author_create'),
    url(r'^authors/author/detail/(?P<pk>\S+)/$', views.AuthorDetailView.as_view(), name='authors_author_detail'),
    url(r'^authors/author/update/(?P<pk>\S+)/$', views.AuthorUpdateView.as_view(), name='authors_author_update'),
)

