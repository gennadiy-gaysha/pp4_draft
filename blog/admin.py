from django.contrib import admin
from .models import Post, Country
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'created_on',)
    list_filter = ('status', 'created_on',)
    search_fields = ('title', 'content',)
    ordering = ('-created_on',)
    summernote_fields = ['content']
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(status=1)

    approve_posts.short_description = "Approve posts"

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['country_name']



