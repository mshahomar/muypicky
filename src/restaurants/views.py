from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView)
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
import random


# def home(request):
#     # html_var = 'f string'
#     # html_ = f"""<!DOCTYPE html>
#     # <html>
#     # <head></head>
#     # <body>
#     #     <h1>Welcome to Home View</h1>
#     #     <p>This is { html_var } coming through</p>
#     # </body>
#     # </html>
#     # """
#     # return HttpResponse(html_)
#     num = None
#     condition_bool = True
#     if condition_bool:
#         num = random.randint(0, 200000)
#     some_list = [
#         random.randint(0, 1000000),
#         random.randint(0, 2000000),
#         random.randint(0, 3000000),
#     ]
#     context = {
#         'num': num,
#         'some_list': some_list
#     }
#     template = 'home.html'
#     return render(request, template, context)
#
#
# def about(request):
#     template = 'about.html'
#     context = {}
#     return render(request, template, context)
#
#
# def contact(request):
#     template = 'contact.html'
#     context = {}
#     return render(request, template, context)
#
#
# # class ContactView(View):
# #     # define which method this View allows for:
# #     def get(self, request, *args, **kwargs):
# #         context = {}
# #         template = 'contact.html'
# #         return render(request, template, context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        num = None
        condition_bool = True
        some_list = [
            random.randint(0, 1000000),
            random.randint(0, 2000000),
            random.randint(0, 3000000),
        ]
        if condition_bool:
            num = random.randint(0, 500000)
            context = {'num': num, 'some_list': some_list}
        # print(context)
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


# def restaurant_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         # 'object_list': [12, 14, 313]
#         'object_list': queryset
#     }
#     return render(request, template_name, context)


class RestaurantListView(ListView):
    # queryset = RestaurantLocation.objects.all()
    template_name = 'restaurants/restaurants_list.html'

    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantListView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class MalaysianListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='Malaysian')
    template_name = 'restaurants/restaurants_list.html'


# class SearchRestaurantListView(ListView):
#     template_name = 'restaurants/restaurants_list.html'
#
#     def get_queryset(self):
#         # queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
#         print(self.kwargs)
#         slug = self.kwargs.get("slug")
#
#         if slug:
#             queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) |
#                 Q(category__icontains=slug)
#             )
#         else:
#             queryset = RestaurantLocation.objects.none()
#
#         return queryset


class RestaurantDetailView(DetailView):
    template_name = "restaurants/restaurants_detail.html"
    queryset = RestaurantLocation.objects.all()

    def get_context_data(self, **kwargs):
        print(self.kwargs)
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     # print("rest_id: ", rest_id)
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)     # or pk = rest_id
    #     return obj
    #
    # def get_queryset(self):
    #     queryset = RestaurantLocation.objects.filter(pk__iexact=self.pk)
    #     return queryset

    # def get_queryset(self):
    #     queryset = RestaurantLocation.objects.filter()
    #     return


# # Bad way of implementing form
# def restaurant_createview(request):
#     template_name = 'restaurants/form.html'
#     # print(request.GET)
#     if request.method == 'GET':
#         print("GET data")
#     if request.method == 'POST':
#         print("POST data")
#         print(request.POST)
#         title = request.POST.get('name')
#         location = request.POST.get('location')
#         category = request.POST.get('category')
#         obj = RestaurantLocation.objects.create(
#             name=title,
#             location=location,
#             category=category
#         )
#         return HttpResponseRedirect("/restaurants/")
#     context = {}
#     return render(request, template_name, context)


# # Django way to implement form
# def restaurant_createview(request):
#     form = RestaurantCreateForm(request.POST or None)
#     errors = None
#
#     # if request.method == 'POST':
#     #     form = RestaurantCreateForm(request.POST)
#     if form.is_valid():
#         obj = RestaurantLocation.objects.create(
#             name=form.cleaned_data.get('name'),
#             location=form.cleaned_data.get('location'),
#             category=form.cleaned_data.get('category')
#         )
#         return HttpResponseRedirect("/restaurants/")
#     if form.errors:
#         # print(form.errors)
#         errors = form.errors
#
#     template_name = "restaurants/form.html"
#     context = {
#         'form': form,
#         'errors': errors
#     }
#     return render(request, template_name, context)


# Better way than the above, by utilizing the ModelForm created in forms.py
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors

    template_name = "restaurants/form.html"
    context = {
        'form': form,
        'errors': errors,
    }
    return render(request, template_name, context)


# This is the BEST way, by using the CreateView
class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/form.html"
    success_url = "/restaurants/"