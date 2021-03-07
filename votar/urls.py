from django.urls import path

from . import views

urlpatterns = [
    path("", views.votar_view, name="votar"),
    path("<int:vota_id>", views.votar_view, name="votar"),
    path("<int:vota_id>/", views.votar_view, name="votar")
]