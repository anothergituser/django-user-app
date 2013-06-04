from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)