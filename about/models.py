from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'),)
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
