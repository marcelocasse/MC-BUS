from django.urls import path
from . import views

urlpatterns = [
    #-- Routes --#
   path('update_horarios',views.update_horarios),
   path('buses',views.mostrar_buses),
   path('bus/<str:sector>',views.get_sector,name='bus'),

   path('',views.index),
   path('base',views.base),

    #-- API --#
   path('api/sectores',views.api_sectores,name='api_sectores'),
   path('api/sector/<int:id_localidad>',views.api_sector_lugar,name='api_sector_lugar'),
   path('api/lugaresfinales/<int:id_lugar>',views.api_lugar_final,name='api_lugar_final'),
   path('api/lugar/<int:id_localidad>/horarios',views.api_lugar_horarios,name='api_lugar_horarios'),

]
