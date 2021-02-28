from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:option_id>", views.option, name="option"),
]