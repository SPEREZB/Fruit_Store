from django.urls import path 
from apps.Fruits.views import Inicio,Fruits
from . import views
urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),   
    path('listar_frutas', Fruits.as_view(), name='listar_frutas'),   
    path('crear_fruits', Fruits.as_view(), name='crear_fruits'),  
]
