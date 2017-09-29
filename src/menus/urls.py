from django.conf.urls import url

from .views import (ItemListView, ItemDetailView,
                    ItemCreateView, ItemUpdateView)


urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='menus_list'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='menus_detail'),
    url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='menus_edit'),
    url(r'^create/$', ItemCreateView.as_view(), name='menus_create'),
]
