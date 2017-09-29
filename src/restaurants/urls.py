from django.conf.urls import url
# from restaurants.views import restaurant_listview
# from restaurants.views import HomeView, AboutView, ContactView, restaurant_createview
from .views import (RestaurantListView,
                    RestaurantDetailView,
                    RestaurantCreateView, RestaurantUpdateView)  # SearchRestaurantListView)


urlpatterns = [
    # url(r'^restaurants/$', restaurant_listview, name='restaurants_list'),
    url(r'^$', RestaurantListView.as_view(), name='restaurants_list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^restaurants/create/$', restaurant_createview, name='create'),
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
    # url(r'^malaysian/$', MalaysianListView.as_view(), name='malaysian_list'),
    # url(r'^restaurants/(?P<pk>\d+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),
    # url(r'^restaurants/(?P<rest_id>\d+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='restaurants_edit'),
]
