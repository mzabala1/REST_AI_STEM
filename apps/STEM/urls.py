from django.urls import path
from .views import index, estudiante_view, estudiante_list

urlpatterns = [
    path(r'', index, name="index"),
    path(r'registro', estudiante_view, name="registro_estudiante"),
    path(r'listar', estudiante_list, name="listar_estudiantes"),
]