from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget

from accounts.models import UserProfile
from blog.models import Country


class RegisterForm(UserCreationForm):
    # username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.",
                                        code='invalid', params={'value': email},
                                        )
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"class": "form-control"})
        self.fields['password1'].help_text = ''
        self.fields['password1'].help_text = '* Your password can’t be ' \
                                             'too ' \
                                             'similar to your other personal ' \
                                             'information.<br>* Your password ' \
                                             'must contain at least 8 ' \
                                             'characters.<br>* Your password ' \
                                             'can’t be a commonly used ' \
                                             'password.<br>* Your password ' \
                                             'can’t be entirely numeric.'
        self.fields['password1'].widget.attrs.update({"class": "form-control"})
        self.fields['password2'].widget.attrs.update({"class": "form-control"})
        self.fields[
            'username'].help_text = '<span>*Required. 150 characters or ' \
                                    'fewer. Letters, digits and @/./+/-/_ ' \
                                    'only.</span><br><span style="color: green">*Disclaimer: ' \
                                    'Once created, you cannot change your ' \
                                    'username.</span>'


class UserDetailsForm(UserChangeForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    date_joined = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"class": "form-control"})


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({"class": "form-control"})
        self.fields['new_password1'].widget.attrs.update({"class": "form-control"})
        self.fields['new_password2'].widget.attrs.update({"class": "form-control"})


class UserProfileForm(forms.ModelForm):
    home_country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('country_name'),
                                          widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = UserProfile
        fields = (
            'profile_picture', 'bio', 'home_country', 'gender', 'date_of_birth', 'instagram_profile', 'twitter_profile',
            'facebook_profile', 'linkedin_profile')

        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': SummernoteWidget(),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'home_country': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_profile': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_profile': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook_profile': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_profile': forms.URLInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            'date_of_birth'].help_text = '<span style="color: green">YYYY-MM-DD (please, follow this date format)'
