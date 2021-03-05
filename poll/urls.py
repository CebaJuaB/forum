from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:poll_id>", views.poll_view, name="poll"),
] 