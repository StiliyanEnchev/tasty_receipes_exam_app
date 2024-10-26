from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_profile
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home-page.html'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('home-page')


class ProfileDetails(DetailView):
    template_name = 'details-profile.html'
    form_class = ProfileCreateForm

    def get_object(self, queryset=None):
        get_profile()

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    template_name = 'delete-profile.html'
    model = Profile
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_profile()