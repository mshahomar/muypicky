from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

User = get_user_model()


class ProfileDetailView(DetailView):
    # queryset = User.objects.filter(is_active=True) #not required since we already have method get_object() defined
    template_name = 'profiles/user.html'

    def get_object(self, queryset=None):
        username = self.request.user
        # username = self.kwargs.get('username')
        # user = get_object_or_404(User, username__iexact=username)
        # print("Returned by get_object_or_404: ", user)
        if username is None:
            raise Http404
        # return username
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        print(context)

