from django.urls import path
from . import views

urlpatterns = [
    #-- Routes --#
    path('',views.base),

    #-- API --#
    path('api/sectores',views.api_sectores),
    path('api/bus/<int:id>',views.api_bus),
    path('api/parada/<int:id>/horarios',views.api_parada_horarios),
]
