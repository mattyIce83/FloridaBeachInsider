from django.conf.urls import url

from . import views

urlpatterns = (
    # urls for Image
    url(r'^images/image/$', views.ImageListView.as_view(), name='images_image_list'),
    url(r'^images/image/create/$', views.ImageCreateView.as_view(), name='images_image_create'),
    url(r'^images/image/detail/(?P<pk>\S+)/$', views.ImageDetailView.as_view(), name='images_image_detail'),
    url(r'^images/image/update/(?P<pk>\S+)/$', views.ImageUpdateView.as_view(), name='images_image_update'),
)

