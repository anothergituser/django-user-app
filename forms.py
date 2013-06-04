# coding=utf-8
from django import forms
from django.forms import ModelForm
from accounts.models import UserProfile
from django.contrib.auth.models import User

class CreateUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['email'].required=True

    # override save method becase the password needs to be
    # hashed by the function set_password
    def save(self, commit=True):
        # don't commit to db because there's no password yet
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

# when editing don't want to edit the username, just the password
# and email, that's why two forms for User
class EditUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required=True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['address'].label = "Direccion (opcional)"
        self.fields['telefono'].label = "Telefono (opcional)"
        self.fields['visible'].label = "Enseñar mi telefono y nombre en mi anuncio."

    class Meta:
        model = UserProfile
        exclude = ['user',]