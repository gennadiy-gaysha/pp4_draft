from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from blog.models import Country


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              blank=True)
    home_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    instagram_profile = models.URLField(blank=True)
    twitter_profile = models.URLField(blank=True)
    facebook_profile = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    # Add fields from the User model
    username = models.CharField(max_length=150, default='my_unique_username')
    email = models.EmailField(default='my_email@my_domain')
    first_name = models.CharField(max_length=30, default='my_name')
    last_name = models.CharField(max_length=150, default='my_surname')


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('author-bio', args=(str(self.user),))
