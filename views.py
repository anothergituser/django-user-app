from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

from accounts.forms import UserProfileForm, CreateUserForm, EditUserForm


@login_required
def profile(request):
    # fetch user from db
    user = User.objects.get(pk=request.user.id)
    
    # save the forms
    if request.method == "POST":
        # create the form to edit the user
        uform = EditUserForm(data=request.POST, instance=user)
        # also edit the profile of this user
        pform = UserProfileForm(data=request.POST, instance=request.user.get_profile())

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'User udated.')
        else:
            messages.success(request, 'There was an error.')

    else:
        # create the form to edit the user
        uform = EditUserForm(instance=user)
        # also edit the profile of this user
        pform = UserProfileForm(instance=request.user.get_profile())
        
    ctx = {
        'user_form':uform,
        'profile_form':pform,
    }
    
    return render(request, 'accounts/profile.html', ctx)    
    

def register(request):
    if request.method == "POST":
        uform = CreateUserForm(request.POST)
        pform = UserProfileForm(request.POST)
        if uform.is_valid() and pform.is_valid():
            # create the user and redirect to profile
            user = uform.save()
            profile = pform.save(commit=False)
            profile.user = user
            profile.save()
            # this would be usefull when the profile is 
            # allready created when post_save is triggered
            # profile = user.get_profile()
            # profile.address = pform.cleaned_data['address']
            # profile.save()
            
            # login the user automatically after registering
            user = authenticate(username=user.username, password=uform.cleaned_data['password'])
            login(request, user)
            
            return HttpResponseRedirect(reverse('fi_home'))
    else:
        uform = CreateUserForm()
        pform = UserProfileForm()

    ctx = {
        'user_form':uform,
        'profile_form':pform,
    }
            
    return render(request, 'accounts/register.html', ctx)