from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'),)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return self.title
