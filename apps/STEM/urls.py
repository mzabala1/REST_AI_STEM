from django.contrib import admin
from django.urls import path
from apps.STEM import views
urlpatterns = [
    path('index/', views.index, name="index"),
]
