from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['bio']


class ProfileEditForm(ProfileBaseForm):
    pass
