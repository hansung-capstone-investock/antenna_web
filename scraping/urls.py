from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.parse_dc),
]
