from django.urls import path
from . import views

urlpatterns = [
    path("de", views.learning_data_entry, name="til_de"),
    path("", views.landing_page, name="til_landing"),
]
