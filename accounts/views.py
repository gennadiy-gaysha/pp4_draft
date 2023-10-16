# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import RegisterForm, ChangePasswordForm, UserProfileForm, UserDetailsForm
from accounts.models import UserProfile

from django.contrib.auth.signals import user_logged_in, user_logged_out

class RegisterNewAccount(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        messages.success(self.request, 'Account registered successfully.')
        return super().form_valid(form)

def login_success(sender, request, user, **kwargs):
    messages.success(request, 'You have been logged in successfully.')

def logout_success(sender, request, user, **kwargs):
    messages.success(request, 'You have been logged out successfully.')

# Connect the signal handlers
user_logged_in.connect(login_success)
user_logged_out.connect(logout_success)

class EditDetails(UpdateView):
    form_class = UserDetailsForm
    template_name = 'registration/edit_details.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Details have been updated successfully.')
        return super().form_valid(form)


class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully.')
        return super().form_valid(form)


def author_bio(request, author_name):
    # Get the User and UserProfile objects based on author_name
    author = User.objects.get(username=author_name)
    userprofile = UserProfile.objects.get(user=author)

    # Render the author's bio page template
    return render(request, 'registration/author_bio.html', {'author': author, 'userprofile': userprofile})


class CreateProfile(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'registration/create_profile.html'

    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile created successfully.')
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Exclude fields as needed
        fields_to_exclude = ['username', 'first_name', 'last_name', 'email']
        for field_name in fields_to_exclude:
            form.fields.pop(field_name, None)
        return form


class UpdateProfile(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'registration/update_profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)
    # fields = ['date_of_birth', 'bio', 'gender', 'home_country']

    def get_object(self):
        # get_object is being overriden here
        # Retrieve the UserProfile based on the username from the URL
        # this line extracts the username from the URL
        username = self.kwargs['username']
        # this line retrieves the User object with the specified username;
        # if a user with that username is not found, a 404 error is raised.
        user = get_object_or_404(User, username=username)
        # returns the associated userprofile by accessing it through the
        # user object. The UserProfile model is linked to the User model
        # via a OneToOneField. So, you can access the associated profile
        # through user.userprofile
        return user.userprofile

