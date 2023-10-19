from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('title',)
    search_fields = ('title', 'content',)
    summernote_fields = ['content']
    actions = ['approve_about', 'disapprove_about']

    def approve_about(self, request, queryset):
        queryset.update(status=1)

    def disapprove_about(self, request, queryset):
        queryset.update(status=0)

    approve_about.short_description = "Approve about"
    disapprove_about.short_description = "Disapprove about"




