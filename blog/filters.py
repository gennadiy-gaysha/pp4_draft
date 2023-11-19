import django_filters
from django import forms

from .models import Post, Country


class PostFilter(django_filters.FilterSet):
    """
    Filter class for filtering Post objects based on the selected country.

    Attributes:
        country: django_filters.ModelChoiceFilter
            A filter for selecting the country from a list of all countries.
            The queryset is ordered by country name.
            The filter is represented as a dropdown select form element.
    """
    country = django_filters.ModelChoiceFilter(
        queryset=Country.objects.all().order_by('country_name'),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 20%; display: inline;'}),

    )

    class Meta:
        model = Post
        fields = ['country']
