from django.urls import path
from . import views

urlpatterns = [
    #-- Routes --#
   path('update_horarios',views.update_horarios),
   path('buses',views.mostrar_buses),
   path('bus/<str:sector>',views.get_sector,name='bus'),

   path('',views.index),

    #-- API --#
   path('api/sector',views.api_sector,name='api_sector'),
   path('api/sector/<int:id_sector>',views.api_sector_lugar,name='api_sector_lugar'),
   path('api/lugaresfinales/<int:id_lugar>',views.api_lugar_final,name='api_lugar_final'),
   path('api/lugar/<int:id_sector>/horarios',views.api_lugar_horarios,name='api_lugar_horarios'),

]
