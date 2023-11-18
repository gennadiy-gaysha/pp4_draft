from django import forms
from .models import Post, Country
from django_summernote.widgets import SummernoteWidget

countries = Country.objects.all().values_list('country_name', 'country_name')
countries_list = []
for country in countries:
    countries_list.append(country)


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        countries = Country.objects.all().order_by('country_name')
        self.fields['country'].queryset = countries
        self.fields['status'].choices = [(0, 'Save as draft'),
                                         (1, 'Send to moderation')]

    class Meta:
        model = Post
        fields = ('country', 'title', 'featured_image', 'content', 'status')
        widgets = {
            'country': forms.Select(choices=countries_list, attrs={'class': 'form-control', 'style': 'width: 100%'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'content': SummernoteWidget(),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%'})
            # 'content': forms.Textarea(attrs={'class': 'form-control'})
        }


