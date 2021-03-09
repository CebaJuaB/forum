from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="votar"),
    path("<int:poll_id>", views.voto_view, name="voto")
]