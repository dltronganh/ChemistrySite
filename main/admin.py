from django.contrib import admin
from tinymce.widgets import TinyMCE
# Register your models here.
from django.db import models
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["lecture_title", "lecture_published"]}),
        ("URL", {'fields': ["lecture_slug"]}),
        ("Series", {'fields': ["lecture_series"]}),
        ("Content", {"fields": ["lecture_content"]})
    ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Lecture,LectureAdmin)
