from django.urls import path
from .views import index, estudiante_view, estudiante_list, estudianteFullList, estudianteRudView

app_name = "REST_AI_STEM"

urlpatterns = [
    path('', index, name="index"),
    path('registro/', estudiante_view, name="registro_estudiante"),
    path('listar/', estudiante_list, name="listar_estudiantes"),
    path('api/', estudianteFullList.as_view(), name='estudiante-list'),
    path('api/<pk>/', estudianteRudView.as_view(), name='estudiante-rud'),
]
