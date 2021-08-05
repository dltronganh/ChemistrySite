from django.db import models
from datetime import datetime

# Create your models here.
class LectureCategory(models.Model):

    lecture_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.lecture_category

class LectureSeries(models.Model):
    lecture_series = models.CharField(max_length=200)
    lecture_category = models.ForeignKey(LectureCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.lecture_series

class Lecture(models.Model):
    lecture_title = models.CharField(max_length=200)
    lecture_content = models.TextField()
    lecture_published = models.DateTimeField('date published')
    lecture_series = models.ForeignKey(LectureSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    lecture_slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.lecture_title