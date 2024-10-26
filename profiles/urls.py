from django.urls import path

from profiles.views import HomePage, ProfileCreateView

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('create/', ProfileCreateView.as_view(), name='create-profile')]