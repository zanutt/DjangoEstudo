from django.urls import path
#quando usamos . contamos que estamos na mesma pasta do arquivo
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"), 
]