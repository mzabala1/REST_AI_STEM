from django.contrib import admin
from django.urls import path, include
from STEM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('STEM.urls')),
    path('estudiantes/', views.EstudianteList.as_view()),
]
