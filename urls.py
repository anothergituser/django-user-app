from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',
    # authentication stuff
    url(r'^login/$', 
        'django.contrib.auth.views.login', 
        {'template_name': 'accounts/login.html'}, name="ac_login"),
    url(r'^logout/$', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'accounts/logged_out.html', 'next_page':'/'}, name="ac_logout"),
    # user profile
    url(r'^profile/$', views.profile, name='ac_profile'),
    # create user
    url(r'^register/$', views.register, name='ac_register'),
)