from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:poll_id>", views.poll_view, name="poll"),
    path("<int:poll_id>/", views.poll_view, name="poll"),
    path("<int:vota_id>", views.votar_view, name="votar"),
    path("<int:vota_id>/", views.votar_view, name="votar")
] 