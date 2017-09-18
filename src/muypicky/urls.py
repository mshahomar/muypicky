"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# from restaurants.views import home, about, contact,
# from restaurants.views import restaurant_listview
from restaurants.views import HomeView, AboutView, ContactView, restaurant_createview
from restaurants.views import (RestaurantListView,
                               # SearchRestaurantListView,
                               MalaysianListView,
                               RestaurantDetailView,
                               RestaurantCreateView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', home, name='home'),
    # url(r'^about/$', about, name='about'),
    # url(r'^contact/$', contact, name='contact'),
    # url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    # url(r'^restaurants/$', restaurant_listview, name='restaurants_list'),
    url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants_list'),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='create'),
    # url(r'^restaurants/create/$', restaurant_createview, name='create'),
    # url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
    url(r'^restaurants/malaysian/$', MalaysianListView.as_view(), name='malaysian_list'),
    # url(r'^restaurants/(?P<pk>\d+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),
    # url(r'^restaurants/(?P<rest_id>\d+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurants_detail'),

]
