from django.contrib import admin
from django.urls import path, include

app_name = "REST_AI_STEM"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('STEM.urls', namespace="app-stem")),
]
