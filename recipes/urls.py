from django.urls import path
#quando usamos . contamos que estamos na mesma pasta do arquivo
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe), 
]