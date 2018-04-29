from django.urls import path
from .views import index, estudiante_view

urlpatterns = [
    path(r'', index, name="index"),
    path(r'registro', estudiante_view, name="registro_estudiante"),
]
