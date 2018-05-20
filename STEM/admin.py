from django.contrib import admin

from .models import Estudiante
from .models import Predecidos

admin.site.register(Predecidos)
admin.site.register(Estudiante)
