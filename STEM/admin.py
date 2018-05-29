from django.contrib import admin

from .models import Estudiante, Predecidos, Preguntas

admin.site.register(Predecidos)
admin.site.register(Estudiante)
admin.site.register(Preguntas)
