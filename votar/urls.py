from django.urls import path

from . import views

urlpatterns = [
    path("", views.votar_view, name="votar"),
    path("<int:poll_id>", views.vota_view, name="votar")
]