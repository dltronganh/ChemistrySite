from django.db import models
from datetime import datetime

# Create your models here.
class Lecture(models.Model):
    lecture_title = models.CharField(max_length=2000)
    lecture_content = models.TextField()
    lecture_published = models.DateTimeField('date published',default=datetime.now)
    

    def __str__(self):
        return self.lecture_title