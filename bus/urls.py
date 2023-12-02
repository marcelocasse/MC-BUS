from django.urls import path
from . import views

urlpatterns = [
    #-- Routes --#
#    path('update_horarios',views.update_horarios),
#    path('buses',views.mostrar_buses),
#    path('bus/<str:sector>',views.get_sector,name='bus'),

   path('',views.base),

    path('api/sectores',views.api_sectores),
    path('api/bus/<int:id>',views.api_bus),
    path('api/parada/<int:id>/horarios',views.api_parada_horarios),
    #-- API --#
    # path('api/buses',views.api_buses,name='api_buses'),
    # path('api/bus/<int:id_bus>',views.api_bus_paradas,name='api_bus_paradas'),
    # path('api/bus/<int:id_bus>/parada/<int:id_parada>/horarios',views.api_parada_horarios,name='api_parada_horarios'),
    # path('api/bus/<int:id_bus>/paradasfinales/<int:id_parada>',views.api_parada_final,name='api_parada_final'),

]
