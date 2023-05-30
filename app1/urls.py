from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('apfelbaum/', views.apfelbaum, name="apfelbaum"),
    path('apfelbaum/<str:name>/<int:number>', views.apfelbaum_n, name="apfelbaum"),
    path('mutter/<int:id>', views.mutter, name="mutter"),
    path('familie/', views.familie, name="familie"),
]