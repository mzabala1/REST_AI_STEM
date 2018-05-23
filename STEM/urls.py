from django.urls import path
from .views import index, estudiante_view, estudiante_list, estudianteFullList, estudianteRudView, predecidosFullList, predecidosRudView, registro_preguntas, descargar_apk

app_name = "REST_AI_STEM"

urlpatterns = [
    path('', index, name="index"),
    path('registro/estudiante', estudiante_view, name="registro_estudiante"),
    path('listar/', estudiante_list, name="listar_estudiantes"),
    path('api/estudiante/', estudianteFullList.as_view(), name='estudiante-list'),
    path('api/estudiante/<pk>/', estudianteRudView.as_view(), name='estudiante-rud'),
    path('api/predecidos/', predecidosFullList.as_view(), name='predecidos-list'),
    path('api/predecidos/<pk>/', predecidosRudView.as_view(), name='predecidos-rud'),
    path('registro/pregunta', registro_preguntas, name='registro-preguntas'),
    path('apk/', descargar_apk, name='descargar-apk'),
]
