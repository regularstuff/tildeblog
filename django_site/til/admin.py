from django.contrib import admin

from .models import Learned, LearningTag

# this will add the post link on the admin page
admin.site.register(Learned)
admin.site.register(LearningTag)