from django.conf.urls import url

from .views import (ItemListView, ItemDetailView,
                    ItemCreateView, ItemUpdateView)


urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='menus_list'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='menus_detail'),
    url(r'^create/$', ItemCreateView.as_view(), name='menus_create'),
    url(r'^edit/(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='menus_edit'),
]
