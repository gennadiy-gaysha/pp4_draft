import django_filters
from django import forms

from .models import Post, Country


class PostFilter(django_filters.FilterSet):
    country = django_filters.ModelChoiceFilter(
        queryset=Country.objects.all().order_by('country_name'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 20%; display: inline;', 'label': 'Filter posts by country: '}),
        label='Filter by country',
    )

    class Meta:
        model = Post
        fields = ['country']
