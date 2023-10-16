from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0, 'Draft'), (1, 'Published'),)


class Country(models.Model):
    iso = models.CharField(max_length=5, default='')
    iso3 = models.CharField(max_length=5, default='')
    iso_numeric = models.CharField(max_length=5, default='')
    fips = models.CharField(max_length=5, default='')
    country_name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    capital = models.CharField(max_length=100, default='')
    area_sq_km = models.FloatField(default=0.0)
    population = models.IntegerField(default=0)
    continent = models.CharField(max_length=5, default='')
    tld = models.CharField(max_length=5, blank=True, default='')
    currency_code = models.CharField(max_length=5, default='')
    currency_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    postal_code_format = models.CharField(max_length=100, default='')
    postal_code_regex = models.CharField(max_length=100, default='')
    languages = models.CharField(max_length=100, default='')
    geonameid = models.IntegerField(default=0)
    neighbours = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.country_name
    def save(self, *args, **qwargs):
        if not self.slug:
            self.slug = slugify(self.country_name)
        super().save(*args, **qwargs)



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def save(self, *args, **kwargs):
        """
        Save method of the model is being overriden. Inside the save method,
        the condition if the slug is not already set (i.e., it's blank) is checked.
        If it's blank, a slug from the title is generated using slugify and then
        save the model. This ensures that the slug is automatically created from
        the title when a new post is created.
        """
        if not self.slug:  # Check if slug is not already set
            self.slug = slugify(self.title)  # Generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Calling the get_absolute_url method in Django templates or views generates
        the absolute URL for a specific model instance, e.g.
        <a href="{{ post.get_absolute_url }}" class="post-link"> generates
        http://127.0.0.1:8000/post/slug_name/
        get_absolute_url method provides the URL to which Django will redirect the
        user after the successful creation of a new post, allowing Django's built-in
        view handling to take care of the actual redirection to the post-details view
        and template. slug here is from urls.py path:
        path('post/<slug:slug>/', views.PostDetails.as_view(), name='post-details')
        """
        return reverse('post-details', args=(str(self.slug),))
