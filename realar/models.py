from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


from .choices import *

class List (models.Model):
    title = models.CharField (max_length=200)
    address = models.CharField (max_length=200)
    city = models.CharField (max_length=100)
    state = state = models.CharField(max_length=20, choices=state_choices.items())
    zipcode = models.CharField (max_length=20)
    description = models.TextField (blank=True)
    price = models.IntegerField ()
    bedrooms = models.IntegerField ()
    bathrooms = models.DecimalField (max_digits=2, decimal_places=1)
    garage = models.IntegerField (default=0)
    sqft = models.IntegerField ()
    lot_size = models.DecimalField (max_digits=5, decimal_places=1)
    photo_main = models.ImageField (upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField (default=True)
    list_data = models.DateTimeField (default=datetime.now, blank=True)
    youtube_video_url = models.URLField(blank=True, null=True)
    google_profile_url = models.URLField(blank=True, null=True)



    def __str__(self):
        return self.title




STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField('Text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



