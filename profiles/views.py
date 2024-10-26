from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from profiles.forms import ProfileCreateForm
from profiles.models import Profile


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home-page.html'

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('home-page')