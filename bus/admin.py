from django.contrib import admin
from .models import HorarioPorDia,Dia,Horario, BusSchedule

# Register your models here.
admin.site.register(BusSchedule)
# admin.site.register(Time)
admin.site.register(HorarioPorDia)
admin.site.register(Dia)
admin.site.register(Horario)