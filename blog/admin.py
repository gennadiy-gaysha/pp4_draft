from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'created_on',)
    list_filter = ('status', 'created_on',)
    search_fields = ('title', 'content',)
    ordering = ('-created_on',)

    summernote_fields = ['content']

# admin.site.register(Post)
