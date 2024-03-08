from django.contrib import admin

from .models import Learned, LearningTag


class LearnedAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'tldr', 'created']

# this will add view and edit functionality on the admin page
admin.site.register(Learned, LearnedAdmin)
admin.site.register(LearningTag)