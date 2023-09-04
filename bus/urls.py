from django.urls import path
from . import views

urlpatterns = [
    path('bus',views.newbus,name='bus'),
    path('get_horarios',views.get_horarios,name='get_horarios'),
    path('get_dias',views.get_dias,name='get_dias'),
    path('update_horarios',views.update_horarios,name='update_horarios'),
    path('update_horariospordia',views.update_horariopordia,name='update_horariospordia'),
    
    
    path('prueba',views.prueba,name='prueba'),
]
