from django.db import models
from datetime import datetime

from django.db.models.base import Model

# Create your models here.
class PostCategory(models.Model):
    post_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1) #ulr that point to this category

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.post_category

class PostSeries(models.Model):
    post_series = models.CharField(max_length=200)
    post_category = models.ForeignKey(PostCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"
    
    def __str__(self):
        return self.post_series

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_published = models.DateTimeField('Data published', default=datetime.now)
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    post_series = models.ForeignKey(PostSeries, default=1, verbose_name= "Series", on_delete=models.SET_DEFAULT)
    post_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.post_title