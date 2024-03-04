from django.urls import path
from . import views

urlpatterns = [
    path("de", views.learning_data_entry, name="til_de"),
    path("show/<int:learnt_id>", views.show, name="til_show"),
    path("", views.landing_page, name="til_landing"),
]
