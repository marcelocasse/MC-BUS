from django.urls import path
from . import views

urlpatterns = [
    #-- Routes --#
   path('update_horarios',views.update_horarios),
   path('buses',views.mostrar_buses)

]
