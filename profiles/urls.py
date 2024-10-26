from django.urls import path

from profiles.views import HomePage, ProfileCreateView, ProfileDetails, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('create/', ProfileCreateView.as_view(), name='create-profile'),
    path('details/', ProfileDetails.as_view(), name='profile-details'),
    path('edit/', ProfileEditView.as_view(), name='edit-profile'),
    path('delete/', ProfileDeleteView.as_view(), name='delete-profile')

]