from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create a user profile to store aditional information
# like address
class UserProfile(models.Model):
    # relation to User model
    user = models.OneToOneField(User)
    address = models.CharField("Direccion", max_length=255)
    telefono = models.CharField("Telefono", max_length=20, null=True)
    visible = models.BooleanField()

# automatically create a profile for a user when created
# connect to the post_save signal of the User model
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# connect only to the post_save signal of User model
#post_save.connect(create_user_profile, sender=User)