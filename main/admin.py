from django.contrib import admin
from .models import Post, PostCategory, PostSeries

from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # fields = [
    #     "post_title",
    #     "post_content",
    #     "post_published",
    # ]

    fieldsets = [
        ("Title/date", {'fields': ["post_title", "post_published"]}),
        ("URL", {'fields': ["post_slug"]}),
        ("Series", {'fields': ["post_series"]}),
        ("Content", {"fields": ["post_content"]}),

    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(PostSeries)
admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)