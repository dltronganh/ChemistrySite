from django.contrib import admin
from tinymce.widgets import TinyMCE
# Register your models here.
from django.db import models
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["lecture_title", "lecture_published"]}),
        ("Content", {"fields": ["lecture_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }
admin.site.register(Lecture,LectureAdmin)
