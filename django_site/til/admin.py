from django.contrib import admin

from .models import Learned, LearningTag

# these classes are allowing visual aids in the admin view.
# and also if indicated will allow you to search the respective areas, i.e. name or title.
class LearnedAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'tldr', 'created']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


# this will add view and edit functionality on the admin page
admin.site.register(Learned, LearnedAdmin)
admin.site.register(LearningTag, TagAdmin)